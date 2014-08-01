#coding=utf-8
#Redis实现用户系统
__author__ = 'beginman'
import redis
import datetime
import hashlib
r = redis.StrictRedis(host='localhost', port='6379', db=0)

class usSystem(object):
    def __init__(self, request,response=None, uid=0, **kwargs):
        self.request = request
        self.response = response
        self.kwargs = kwargs
        self.uid = uid          # user id
        self.sessionid = None

    def testCookie(self):
        """事先在登陆方法中下了request.session.set_test_cookie()的套子"""
        if self.request.session.test_cookie_worked():
            self.request.session.delete_test_cookie()
            return True
        return False

    def getUsObj(self):
        """返回用户对象,有则说明用户已登陆,无则注销"""
        self.sessionid = self.request.COOKIES.get('sessionid', None)
        if r.exists(self.sessionid):
            if r.exists('sessionid_%s' %self.sessionid):
                return r.hget('sessionid_%s' %self.sessionid, 'uid')
        return None

    def setCookieAndSession(self):
        """cookie在登陆成功后已经写入"""
        self.sessionid = self.request.COOKIES.get('sessionid', None)
        if not self.sessionid:
            # set cookie
            h = hashlib.md5()
            h.update(datetime.datetime.now())
            self.response.set_cookie('sessionid', h.hexdigest())
            self.sessionid = h.hexdigest()

        if not r.exists('sessionid_%s' %self.sessionid):
            #set session
            r.hset('sessionid_%s' %self.sessionid,'uid', self.uid)

        return True






