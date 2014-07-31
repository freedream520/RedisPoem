# coding=utf-8
__author__ = 'beginman'
import redis
r = redis.StrictRedis(host='localhost', port='6379', db=0)

class comGetAndSet(object):
    def __init__(self, key, value, **kwargs):
        self.key = key
        self.value = value
        self.kwargs = kwargs

    def set(self):
        return r.set(self.key, self.value)

    def get(self):
        return r.get(self.key) or None

