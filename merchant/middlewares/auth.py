from django.utils.deprecation import MiddlewareMixin

from django.shortcuts import render, redirect

class AuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        ## 页面排除，login页面不需要鉴权

        url=["/send/logincode/","/user/login/"]
        if request.path_info in url:
            return  #通过
        if request.session.get('login_status') is None:
            return redirect('/user/login/')  #不通过