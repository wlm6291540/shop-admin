import hashlib
import os
import random
import datetime
import sys

from PIL import Image

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import TemplateView

from shop_admin import settings
from system.models import Menu
from system.serializers.serializers_menu import MenuTreeSerializer


class LoginPageView(TemplateView):
    template_name = 'views/user/login.html'


class MainPageView(TemplateView):
    template_name = 'views/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['user'] = user
        queryset = Menu.objects.filter(parent=None).all()
        serializer = MenuTreeSerializer(queryset, many=True)
        context['menus'] = serializer.data
        return context


class ConsolePageView(TemplateView):
    template_name = 'views/home/console.html'


class ImageUploadView(View):
    def post(self, request):
        code = 0
        msg = '上传成功'
        data = None
        try:
            image = request.FILES['file']
            # 需要判断文件类型是否是图片.
            name = image.name
            image = Image.open(image)
            w, h = image.size
            if w >= h:
                w_start = (w - h) * 0.618
                box = (w_start, 0, w_start + h, h)
                region = image.crop(box)
            else:
                h_start = (h - w) * 0.618
                box = (0, h_start, w, h_start + w)
                region = image.crop(box)

            location = str(name).find('.')
            extension = name[location:]

            name = name[:location] + str(datetime.datetime.now()) + str(random.random())
            md5 = hashlib.md5(name.encode('utf-8')).hexdigest()
            image.name = md5[:10] + extension
            path_name = os.path.join(settings.MEDIA_ROOT, 'shop/brand/')
            if not os.path.exists(path_name):
                os.makedirs(path_name)
            with open(path_name + image.name, 'w') as file:
                image.save(file)
            data = {'url': settings.MEDIA_URL + 'shop/brand/' + image.name}
        except Exception as e:
            code = 1
            msg = '系统内部错误'
            print(e)
        ret = dict(code=code, msg=msg, data=data)
        return JsonResponse(ret)
