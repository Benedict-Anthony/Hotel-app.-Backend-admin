from django.shortcuts import render
from rest_framework.views import APIView
from accommodation.models import AccommodationSpace
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.parsers import MultiPartParser, FormParser


from accommodation.serializer import (AccommodationCategorySerializer, AccommodationCreateSerializer,
                                      AccommodationSpaceDetailSerializer,
                                      AccommodationSpaceSerializer)

class AccommodationListView(APIView):
    serializer_class = AccommodationSpaceSerializer
    
    def get(self, request, *args, **kwargs):
        
        slug = kwargs.get("slug")
        if slug:
            queryset = AccommodationSpace.accomodation.get(slug=slug)
            serializer = AccommodationSpaceDetailSerializer(queryset).data
            return Response(serializer)
        
        
        quaryset = AccommodationSpace.accomodation.all().order_by("-created_at")
        serializer = self.serializer_class(quaryset, many=True).data
        return Response(serializer)
    
    
    
class AccommodationMutateView(APIView):
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = AccommodationCreateSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    

    
    def put(self, request, id):
        try:
            quaryset = AccommodationSpace.objects.get(id=id)
            if quaryset:
                serializer = self.serializer_class(quaryset, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors)
        except AccommodationSpace.DoesNotExist:
            return Response({"message": 'not found'}, status= status.HTTP_404_NOT_FOUND)
        return Response({"message": 'not found'})
            
            
            
    def delete(self, request, id):
        try:
            quaryset = AccommodationSpace.objects.get(id=id)
        except AccommodationSpace.DoesNotExist:
            return Response({"message": 'not found'}, status= status.HTTP_404_NOT_FOUND)
        if quaryset:
            quaryset.delete()
            return Response({"message": 'deleted successfully'}, status= status.HTTP_204_NO_CONTENT)
        
        return Response({"message": 'not found'})
            
            
class CategoryListView(APIView):
    serializer_class = AccommodationCategorySerializer
    def get(self, request):
        quaryset = AccommodationSpace.accomodation.all()
        serializer = self.serializer_class(quaryset, many=True).data
        return Response(serializer)