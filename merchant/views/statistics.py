from merchant.models import PlatformCategory, XhsOrder, ProductSource
from django.db.models import Sum
from django.shortcuts import render
import json
from decimal import Decimal

def statistics_view(request):
    # 计算每个平台的总收入柱状图
    platforms = PlatformCategory.objects.all()
    platform_income = []
    incomes=0

    for platform in platforms:
        total_income = XhsOrder.objects.filter(platform=platform).aggregate(total=Sum('inaccount'))['total'] or Decimal(0)
        incomes+=total_income
        platform_income.append({'name': platform.name, 'total_income': float(total_income)})
    # 使用 Echarts 展示总收入柱状图
    echarts_data = {
        'title': {'text': '各平台总收入'},
        'xAxis': {'type': 'category', 'data': [item['name'] for item in platform_income]},
        'yAxis': {'type': 'value'},
        'series': [{'data': [item['total_income'] for item in platform_income], 'type': 'bar'}]
    }

    # 计算每个商品的总销量
    product_sales = []
    for product_source in ProductSource.objects.all():
        total_sales = XhsOrder.objects.filter(product_source=product_source.uuid).aggregate(total_sales=Sum('amount'))[
                          'total_sales'] or 0
        product_sales.append({'title': product_source.title, 'total_sales': total_sales})

    # 使用切片操作获取前5名最畅销的商品
    product_sales_top5 = sorted(product_sales, key=lambda x: x['total_sales'], reverse=True)[:5]

    # 使用 Echarts 展示最畅销的几个商品柱状图
    echarts_data_sales = {
        'title': {'text': '最畅销的5个商品'},
        'xAxis': {'type': 'category', 'data': [product['title'] for product in product_sales_top5]},
        'yAxis': {'type': 'value'},
        'series': [{'data': [product['total_sales'] for product in product_sales_top5], 'type': 'bar'}]
    }

    context = {
        'echarts_data': json.dumps(echarts_data),  # 将字典转换为 JSON 字符串
        'echarts_data_sales': json.dumps(echarts_data_sales),  # 将字典转换为 JSON 字符串
        'total_sales': incomes,
    }

    return render(request, 'statistics_template.html', context)
