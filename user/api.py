from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import response
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from .serializers import bookserializer
from rest_framework.response import Response
from django.http import HttpResponse
from django.contrib.auth.models import User


class login_V(APIView):
    # def get(self,request):
        #books=Book.objects.all()#
        #ser=bookserializer(books,many=True)#
        # why use .data#
        #return Response(ser.data)#
    def post(self,request):
        print(request.data)
        username=request.data.get('username', False)
        password=request.data.get('password', False)
        print("username ==> ", username)
        print("pass ==> ", password)
        if not (username and password):
            return HttpResponse('Invalid username or password')
        current_user = get_object_or_404(User,  username=username)
        if not current_user.check_password(password):
            return HttpResponse('Invalid password')
        user = authenticate(username=username,password=password)
        login(request,user)
        return HttpResponse('Login Successfully', status=200)