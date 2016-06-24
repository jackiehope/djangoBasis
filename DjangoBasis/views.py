#coding:utf-8
from django.http import HttpResponse

def hello(request):
    """先来一个国际惯例"""
    return HttpResponse("hello Django")
