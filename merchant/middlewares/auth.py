from django.utils.deprecation import MiddlewareMixin

from django.shortcuts import render, redirect

class AuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        ## 页面排除，login页面不需要鉴权
        if request.path_info == "/user/login/":
            return  #通过
        if request.session.get('username') is None:
            return redirect('/user/login/')  #不通过