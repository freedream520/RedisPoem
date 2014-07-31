# coding=utf-8
__author__ = 'beginman'
from django.shortcuts import render
from django.http import HttpResponseRedirect
# from superRedis import *
from form import LoginForm
import redis
r = redis.StrictRedis(host='localhost', port='6379', db=0)


def home(request):
    return render(request, 'index.html')


def usLogin(request):
    context = {}
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            us = form.cleaned_data['us']
            pwd = form.cleaned_data['pwd']
            red_us = r.get('us')
            red_pwd = r.get('pwd')
            if red_us and red_pwd and red_us == us and red_pwd == pwd:
                return HttpResponseRedirect('/')
        context['msg'] = u'账号或密码错误'
        context['form'] = form


    form = LoginForm()
    context['form'] = form
    return render(request, 'login.html', context)
