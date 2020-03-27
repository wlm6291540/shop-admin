import re

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.deprecation import MiddlewareMixin
from django.contrib.auth import authenticate


class PermissionMiddleWare(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated and request.path.startswith('/login'):
            return redirect('/main/view')
        elif not request.path.startswith("/login") and not request.user.is_authenticated:
            return render(request, "views/user/login.html")
        else:
            if request.path.endswith('/'):
                return
            elif 'logout' in request.path or 'login' in request.path:
                return
            elif 'static' in request.path:
                return
            roles = list(request.user.roles.all())
            menus = []
            for role in roles:
                menus.extend([url['url'] for url in list(role.menus.values('url'))])
            pattern = re.compile('((/[a-z_]+)+)')
            ret = re.match(pattern, request.path)
            if ret:
                ret = ret.groups()[0]
            else:
                ret = request.path
            print(ret)
            if 'view' in request.path and ret not in menus:
                return render(request, '404.html')
            elif ret not in menus:
                return HttpResponse(status=403)
