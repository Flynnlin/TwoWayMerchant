

from django import forms

from merchant.models import PlatformCategory,ProductSource,XhsOrder
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