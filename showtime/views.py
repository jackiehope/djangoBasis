#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import datetime

def showtime(request):
    "显示当前时间"
    now = datetime.datetime.now()
    html = "<html><body>The time now is %s </body></html>" % now
    return HttpResponse(html)
