

from django import forms
from django.conf import settings

from merchant.models import PlatformCategory, ProductSource, XhsOrder, Wiki


class BootstrapModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BootstrapModelForm, self).__init__(*args, **kwargs)
        #循环找到所有的字段，并将他们的插件添加class
        for name,field in self.fields.items():
            if field.widget.attrs:
                field.widget.attrs['class'] = 'form-control'
                field.widget.attrs['placeholder'] ='请输入 %s' % (field.label,)
            else:
                field.widget.attrs = {'class':'form-control'}
class BootstrapForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(BootstrapForm, self).__init__(*args, **kwargs)
        #循环找到所有的字段，并将他们的插件添加class
        for name,field in self.fields.items():
            if field.widget.attrs:
                field.widget.attrs['class'] = 'form-control'
                field.widget.attrs['placeholder'] = '请输入 %s' % (field.label,)
            else:
                field.widget.attrs = {'class':'form-control'}


class UserLogin_code_Form(BootstrapForm):
    username = forms.CharField(max_length=10,required=True)
    password = forms.CharField(max_length=10, widget=forms.PasswordInput, required=True)
    captcha = forms.CharField(widget=forms.TextInput,required=True)
    def user_login(self, request):
        if self.is_valid():
            captcha = self.cleaned_data['captcha']
            if request.session.get('code_txt') != captcha:
                self.add_error('captcha', '验证码错误或者过期')
                return False
            else:
                password = self.cleaned_data['password']
                username = self.cleaned_data['username']
                if password != settings.PASSWORD or username not in settings.USERNAME:
                    self.add_error('password', '用户名或密码错误')
                    return False
                else:
                    return True
        else:
            return False
class PlatformCategoryForm(BootstrapModelForm):
    class Meta:
        model = PlatformCategory
        fields = "__all__"

class ProductSourceForm(BootstrapModelForm):
    class Meta:
        model = ProductSource
        fields = "__all__"
        exclude = ['uuid']

class XhsOrderForm(BootstrapModelForm):
    class Meta:
        model = XhsOrder
        fields = "__all__"
        exclude = ['inaccount','platform']
    def clean_product_source(self):
        if ProductSource.objects.filter(uuid=self.cleaned_data['product_source']).exists():
            return self.cleaned_data['product_source']
        raise forms.ValidationError('商品不存在')
class XhsEditOrderForm(BootstrapModelForm):
    class Meta:
        model = XhsOrder
        fields = "__all__"
    def clean_product_source(self):
        if ProductSource.objects.filter(uuid=self.cleaned_data['product_source']).exists():
            return self.cleaned_data['product_source']
        raise forms.ValidationError('商品不存在')


class WikiModelForm(BootstrapModelForm):
    class Meta:
        model = Wiki
        fields = "__all__"
        exclude = ['product']