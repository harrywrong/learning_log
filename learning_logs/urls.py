"""定义learning_logs的URL模式"""
from django.conf.urls import url
from django.urls import re_path, path
from . import views

urlpatterns = [
    url(r"^$", views.index, name='index'),
    # 脱字符（^ ）让Python查看字符串的开头，而美元符号让Python查看字符串的末尾。总体而言，
    # 这个正则表达式让Python查找开头和末尾之间没有任何东西的URL。
]
