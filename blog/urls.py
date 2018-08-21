# -*- coding: utf-8 -*-
# @Time    : 2018/8/21 11:00
# @Author  : Yuwj
# @File    : urls.py
# @Software: PyCharm

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]