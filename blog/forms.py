# -*- coding: utf-8 -*-
# @Time    : 2018/8/22 15:09
# @Author  : Yuwj
# @File    : forms.py
# @Software: PyCharm

from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
