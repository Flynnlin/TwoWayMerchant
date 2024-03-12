import base64

from django.http import HttpResponse
from django.shortcuts import render, redirect

from merchant.forms import UserLogin_code_Form
from merchant.utils import captcha


def user_login_view(request):
    if request.method == 'POST':
        form = UserLogin_code_Form(request.POST)
        success = form.user_login(request)
        if success:
            request.session['login_status'] = 1
            request.session.set_expiry(7200)
            return redirect('/order/')
        else:
            return render(request, 'user_login.html',
                          {'form': form, 'code_img_io': request.session.get('code_img_io')})

    form = UserLogin_code_Form()
    img_code_view(request)
    return render(request,'user_login.html',
                  {'form':form,'code_img_io': request.session.get('code_img_io')})

def img_code_view(request):
    # 图片验证码生成 每次访问都刷新
    captcha_text, img_io = captcha.generate_captcha()
    img_io_base64 = base64.b64encode(img_io.getvalue()).decode()
    request.session['code_txt'] = captcha_text  # 保存当次验证码
    request.session['code_img_io'] = img_io_base64
    request.session.set_expiry(60)  # 设置超时时间

    return HttpResponse(img_io_base64)