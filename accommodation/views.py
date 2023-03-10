from django.shortcuts import render
from rest_framework.views import APIView
from accommodation.models import Category, Accommodation, Location
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.parsers import MultiPartParser, FormParser


from accommodation.serializer import (CategorySerializer,
                                      AccommodationCreateSerializer,
                                      AccommodationDetailSerializer,
                                      AccommodationSerializer, 
                                      LocationSerializer)

from .permissions import UserWriteOnly

class AccommodationListView(APIView):
    serializer_class = AccommodationSerializer
    def get(self, request, *args, **kwargs):
        slug = kwargs.get("slug")
        if slug:
            queryset = Accommodation.accomodation.get(slug=slug)
            serializer = AccommodationDetailSerializer(queryset).data
            return Response(serializer)
        quaryset = Accommodation.accomodation.all().order_by("-created_at")
        serializer = self.serializer_class(quaryset, many=True).data
        return Response(serializer)
  


class AccommodatioFilterView(APIView):
    serializer_class = AccommodationSerializer
    def get(self,request, category=None, location=None, params=None):
        
        if params:
            queryset = Accommodation.accomodation.search(params)
            serializer = AccommodationSerializer(queryset, many=True).data   
            return Response(serializer)
        
        if location and category:
            try:
                queryset = Accommodation.accomodation.filter(location__name__icontains=location, category__name__icontains=category)
                serializer = AccommodationSerializer(queryset, many=True).data   
                return Response(serializer)
            except Accommodation.DoesNotExist:
                return Response({"message": "No accommodation found"})
            
        if category:
            queryset = Accommodation.accomodation.filter(category__name__icontains=category)
            serializer = AccommodationSerializer(queryset, many=True).data
            return Response(serializer)
            
        if location:
            queryset = Accommodation.accomodation.filter(location__name__icontains=location)
            serializer = AccommodationSerializer(queryset, many=True).data
            return Response(serializer)
        return Response({"message": "No filter params params provided"})
             
    
class AccommodationMutateView(APIView):
    # parser_classes = [MultiPartParser, FormParser]
    permission_classes = [IsAuthenticatedOrReadOnly, UserWriteOnly]
    serializer_class = AccommodationCreateSerializer
    
    def get(self, request):
        user = request.user
        try:
             agent_accommodation_list = Accommodation.objects.filter(agent=user)
        except Accommodation.DoesNotExist:
            return Response({"message": 'not found'}, status= status.HTTP_404_NOT_FOUND)
        
        serializer = self.serializer_class(agent_accommodation_list, many=True).data
        return Response(serializer)
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(agent=request.user)
            return Response(serializer.data)
        return Response(serializer.errors)
    

    
    def put(self, request, slug):
        try:
            quaryset = Accommodation.objects.get(slug=slug)
            if quaryset:
                serializer = self.serializer_class(quaryset, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors)
        except Accommodation.DoesNotExist:
            return Response({"message": 'not found'}, status= status.HTTP_404_NOT_FOUND)
        return Response({"message": 'not found'})
            
            
    
    def patch(self, request, slug):
        try:
            queryset = Accommodation.objects.get(slug=slug)
        except Accommodation.DoesNotExist:
            return Response({"message": 'not found'}, status= status.HTTP_404_NOT_FOUND)
            
        serializer = self.serializer_class(data=request.data, instance=queryset, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    
    def delete(self, request, slug):
        try:
            quaryset = Accommodation.objects.get(slug=slug)
        except Accommodation.DoesNotExist:
            return Response({"message": 'not found'}, status= status.HTTP_404_NOT_FOUND)
        if quaryset:
            quaryset.delete()
            return Response({"message": 'deleted successfully'}, status= status.HTTP_204_NO_CONTENT)
        
        return Response({"message": 'not found'})
            



class CategoryListView(APIView):
    serializer_class = CategorySerializer
    def get(self, request):
        quaryset = Category.objects.all()
        serializer = self.serializer_class(quaryset, many=True).data
        return Response(serializer)
            

class LocationListView(APIView):
    serializer_class = LocationSerializer
    def get(self, request):
        quaryset = Location.objects.all()
        serializer = self.serializer_class(quaryset, many=True).data
        return Response(serializer)