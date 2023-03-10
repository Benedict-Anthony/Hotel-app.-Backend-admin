from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from users.models import CustomUser, HouseAgent

from .serializers import (AgentCreateSerializer, 
                          AgentProfileSerializer, 
                          UserCreationSerializer,
                          UserProfileSerializer)


class UserCreationView(APIView):
    serializer_class = UserCreationSerializer
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        serializer = UserCreationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(is_active=True)
        return Response({"message:": "Account created succesfully"}, status=status.HTTP_201_CREATED)
    


class UserProfileView(APIView):
    serializer_class = AgentCreateSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        user = CustomUser.objects.get(id=request.user.id)
        print(user.id)
        if user.is_agent:
            agent = HouseAgent.objects.get(user=user.id)
            print(agent)
            serializer = AgentProfileSerializer(agent).data
            return Response(serializer)
            
        serializer = UserProfileSerializer(user).data
        return Response(serializer)
    
    def post(self, request):
        user = request.user
        serializer = AgentCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user.is_agent = True
        user.save()
        serializer.save()
        return Response({"massage":"your profile has been upgraded to an agent profile"},status=status.HTTP_201_CREATED)
