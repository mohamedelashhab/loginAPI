from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
import json
from .models import User
from .serializers import (
   
    UserLoginSerializer,
)

class UserLoginAPIView(APIView):
  
    serializer_class = UserLoginSerializer
    

    def post(self, request, *args, **kwargs):
        
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            del new_data['password']
            return Response(new_data)
        return  Response(serializer.errors)

























    

''' def login(request):
    if request.method == 'POST':
        data = request.POST.get("json")
        data = json.loads(data)
        serializer = UserLoginSerializer(data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
        print(data['username'])
    return render(request,'loginAPI/index.html',{}) '''
