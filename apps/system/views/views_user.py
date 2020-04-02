from django.contrib.auth import get_user_model, authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from rest_framework import generics, status
from rest_framework.response import Response

from system.pagination.paginator import CustomPagination
from system.serializers.serializers_user import UserSerializer, UserUpdateSerializer, UserAddSerializer, \
    UserActiveSerializer, UserPasswordUpdateSerializer

User = get_user_model()


class UserPageView(TemplateView):
    template_name = 'views/user/user/list.html'


class UserSetPageView(TemplateView):
    template_name = 'views/set/user/info.html'


class UserPasswordPageView(TemplateView):
    template_name = 'views/set/user/password.html'


class LoginView(View):
    def get(self, request):
        return render(request, 'views/user/login.html')

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse(dict(code=0, msg='登录成功'))
        else:
            return JsonResponse(dict(code=1, msg='用户名或密码错误'))


class LogoutView(View):
    def get(self, request):
        logout(request)
        ret = dict(code=0, msg='退出成功')
        return JsonResponse(ret)


class UserAddView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserAddSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class UserChangeView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer


class UserPasswordChangeView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserPasswordUpdateSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        old_password = request.data.get('old_password', None)
        password = request.data.get('password', None)
        re_password = request.data.get('re_password', None)
        if not request.user.check_password(old_password):
            return Response(dict(msg='当前密码错误'), status=400)
        elif password is not None and password != re_password:
            return Response(dict(msg="两次输入的密码不一致"), status=400)
        else:
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            serializer.validated_data['password'] = make_password(password)
            self.perform_update(serializer)
            user = User.objects.get(id=request.user.id)
            update_session_auth_hash(request, user)

            if getattr(instance, '_prefetched_objects_cache', None):
                instance._prefetched_objects_cache = {}

            return Response(dict(msg='修改成功'), status=200)


class UserActiveView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserActiveSerializer


class UserDeleteView(View):
    pass


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        name = self.request.query_params.get('name', None)
        if name is not None:
            self.queryset = self.queryset.filter(name=name)
        return self.queryset
