# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime

from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView, Response
from celery import task


@task
def test(*args, **kwargs):
    print('args: ', args)
    print('kwargs: ', kwargs)
    print('++++Task started++++')
    for i in range(100):
        print str(i) + ' * ' + str(i) + ' = ' + str(i*i)
    print('====Task ended====')


class TestAPI(APIView):

    def get(self, request, *args, **kwargs):
        print 'got it'
        test.delay('a')
        return Response(data={'info': 'resp: ' + str(datetime.datetime.now())})