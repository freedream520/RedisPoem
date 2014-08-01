#coding=utf-8
#中间件扩展
__author__ = 'beginman'
from django.http import HttpResponseRedirect
from django.conf import settings
from common.userSystem import usSystem


class Mymiddleware(object):
    def process_request(self, request):
        """Request预处理函数"""
        path = str(request.path)
        request.session['domain'] = settings.DOMAIN
        if path.startswith('/site_media/'):
            return None
        #验证登陆
        ussys = usSystem(request)
        if ussys.getUsObj():
            pass





