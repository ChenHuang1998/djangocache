from django.shortcuts import render
from rest_framework_extensions.cache.decorators import cache_response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_extensions.key_constructor import bits
from rest_framework_extensions.key_constructor.bits import UserKeyBit
from rest_framework_extensions.key_constructor.constructors import KeyConstructor

from api.models import UserInfo


class MyKeyConstructor(KeyConstructor):
    all_query_params = bits.QueryParamsKeyBit()
    unique_view_id = bits.UniqueViewIdKeyBit()


class UserView(APIView):
    @cache_response(key_func=MyKeyConstructor())
    def get(self, request):
        id = request.GET.get('id')
        obj = UserInfo.objects.get(id=id)
        print('数据库')
        return Response(obj.username)

class Info(APIView):
    @cache_response(key_func=MyKeyConstructor())
    def get(self, request):
        return Response('ok')