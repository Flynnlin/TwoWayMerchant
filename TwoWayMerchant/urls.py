
"""
URL configuration for TwoWayMerchant project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView

from merchant.views import platform_view, statistics, user_view

urlpatterns = [
    path('', RedirectView.as_view(url='/order/')),
    path('platform/',platform_view.platform_list_view),
    path('platform/add/',platform_view.platform_add_view),
    path('platform/delete/<int:pk>/',platform_view.platform_delete_view),
    path('platform/edit/<int:pk>/',platform_view.platform_edit_view),

    path('merchandise/',platform_view.merchandise_list_view),
    path('merchandise/add/',platform_view.merchandise_add_view),
    path('merchandise/delete/<int:pk>',platform_view.merchandise_delete_view),
    path('merchandise/edit/<int:pk>',platform_view.merchandise_edit_view),
    path('merchandise/mutiladd/',platform_view.merchandise_mutiladd),

    path('order/',platform_view.xhs_order_list_view),
    path('order/add/',platform_view.xhs_order_create_view),
    path('order/detail/<int:pk>/',platform_view.xhs_order_detail_view),
    path('order/edit/<int:pk>',platform_view.xhs_order_update_view),
    path('order/delete/<int:pk>/',platform_view.xhs_order_delete_view),
    # path('/order/mutiladd/')

    path('statistics/',statistics.statistics_view),

    path('user/login/',user_view.user_login_view),
    path('send/logincode/',user_view.img_code_view),
]
