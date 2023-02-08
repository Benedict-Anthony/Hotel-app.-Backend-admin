from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



from .serializers import UserCreationSerializer

import jwt
from django.conf import settings

class UserCreationView(APIView):
    serializer_class = UserCreationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(is_active=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

# def decode_token():
#     print(settings.SECRET_KEY)
#     try:
#         token = jwt.decode("hwRomSyWWqjvVjQ9uF9pcWh2pm32Ox", settings.SECRET_KEY, algorithms=["HS256"])
#         print(token)
#     except Exception as exec:
#         print(exec)
        