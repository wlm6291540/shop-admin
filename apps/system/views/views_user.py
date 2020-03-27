from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from rest_framework import viewsets, serializers, generics, status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from system.pagination.paginator import CustomPagination
from system.serializers.serializers_user import UserSerializer, UserUpdateSerializer, UserAddSerializer, \
    UserActiveSerializer

User = get_user_model()


# class CustomAuthToken(ObtainAuthToken):
#
#     def post(self, request, *args, **kwargs):
#         try:
#             serializer = self.serializer_class(data=request.data,
#                                                context={'request': request})
#             serializer.is_valid(raise_exception=True)
#             user = serializer.validated_data['user']
#             token, created = Token.objects.get_or_create(user=user)
#             request.user = user
#             if token:
#                 code = 0
#                 msg = '登录成功'
#             else:
#                 code = 1
#                 msg = '登录失败'
#         except Exception as e:
#             code = 1
#             msg = str(e)
#         return Response({
#             'code': code,
#             'msg': msg,
#             'data':{
#                 'token': token.key,
#                 'username': user.username,
#                 'user_id': user.id,
#             }
#         })


class UserPageView(TemplateView):
    template_name = 'views/user/user/list.html'


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


class UserChangeView(View):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer


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
