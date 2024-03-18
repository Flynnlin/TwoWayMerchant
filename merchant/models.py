from django.db import models
from mdeditor.fields import MDTextField


# 平台分类
class PlatformCategory(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='平台名')

    def __str__(self):
        return self.name

# 商品源表
class ProductSource(models.Model):
    platform = models.ForeignKey(PlatformCategory, on_delete=models.SET_NULL,null=True,blank=True, verbose_name='平台')
    url = models.CharField(max_length=255,verbose_name='商品链接')
    title = models.CharField(max_length=255, verbose_name='商品标题')
    input_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='进价')
    output_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='出价')
    min_amount = models.PositiveIntegerField(verbose_name='最低数量')
    postage = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='邮费')
    uuid = models.CharField(max_length=32, unique=True, verbose_name='随机字符串')

    def __str__(self):
        return self.title

# xhs订单
class XhsOrder(models.Model):
    orderId = models.CharField(max_length=100, unique=True, verbose_name='订单号')
    platform = models.ForeignKey(PlatformCategory, on_delete=models.SET_NULL,null=True,blank=True, verbose_name='第三方平台')
    platform_orderId = models.CharField(max_length=100, unique=True, verbose_name='第三方订单号')
    inaccount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='收益')
    product_source = models.CharField(max_length=32, unique=True, verbose_name='商品uid')
    amount = models.PositiveIntegerField(verbose_name='购买数量')
    create_datetime = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    def __str__(self):
        return self.orderId


class Wiki(models.Model):
    product = models.ForeignKey(verbose_name='商品', to='ProductSource', on_delete=models.CASCADE)
    title = models.CharField(verbose_name='标题', max_length=32)
    content =MDTextField(verbose_name='内容', blank=True, null=True)

    def __str__(self):
        return self.title
