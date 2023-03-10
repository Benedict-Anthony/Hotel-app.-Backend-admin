from rest_framework import serializers

from accommodation.models import (Category, 
                                  Images, 
                                  Accommodation)
from users.models import CustomUser


class AccommodationAgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "name",
            "phone",
            "email",
        ]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "name",
        ]
        

        
class ImagesSerializer(serializers.ModelSerializer):
    thumbnail = serializers.SerializerMethodField()
    image_url = serializers.SerializerMethodField()
    class Meta:
        model = Images
        fields = [
            "id",
            "image_url",
            "thumbnail"
        ]
        
    def get_thumbnail(self, obj):
        return obj.image_thumbnail()
    
    def get_image_url(self, obj):
        return obj.image_url()
    
    


# ACCOMODATION LOCATION SERIALIZER
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accommodation
        fields = [
            "name",
        ]

# ACCOMMODATION LIST VIEW SERIALIZER
class AccommodationSerializer(serializers.ModelSerializer):
    
    rating = serializers.SerializerMethodField()
    category = CategorySerializer()
    location = LocationSerializer()
    
    class Meta:
        model = Accommodation
        fields = [ "id", "name","category","location","distance","price","banner","rating","available","pinned","created_at","updated_at","slug"
            
        ]
        
    def get_rating(self, obj):
        return obj._rating.count()
    
    # def get_thumbnail(self, obj):
    #     return obj.thumbnail()
        
# ACCOMODATION DETAIL VIEW  SERIALIZER
class AccommodationDetailSerializer(serializers.ModelSerializer):
    images = ImagesSerializer(many=True)
    rating = serializers.SerializerMethodField()
    category = CategorySerializer()
    agent = AccommodationAgentSerializer()
    location = LocationSerializer()
        
    class Meta:
        model = Accommodation
        fields = ["id", "agent","name","distance","description","price","rating","category","location","images", "slug","created_at", "pinned", "available", "updated_at",
        ]
        
    def get_rating(self, obj):
        return obj._rating.count()
    
    
# ACCOMODATION CREATE SERIALIZER

class ImagesCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = [
            "id",
            "image",
        ] 
class AccommodationCreateSerializer(serializers.ModelSerializer):
    images = ImagesCreateSerializer(many=True)
    class Meta:
        model = Accommodation
        fields = ["id","name","category","distance","location","description","banner","price","images","slug","available","pinned"
        ]
        
    def create(self, validated_data):
        images_data = validated_data.pop("images")
        accommodation = Accommodation.objects.create(**validated_data)
        print(images_data)
        for img in images_data:
            image = Images.objects.create(**img)
            accommodation.images.add(image)
        
        accommodation.save()
        return accommodation
    
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.category = validated_data.get("category", instance.category)
        instance.distance = validated_data.get("distance", instance.distance)
        instance.location = validated_data.get("location", instance.location)
        instance.description = validated_data.get("description", instance.description)
        instance.banner = validated_data.get("banner", instance.banner)
        instance.price = validated_data.get("price", instance.price)
        instance.agent = validated_data.get("agent", instance.agent)
        instance.slug = validated_data.get("slug", instance.slug)
        instance.available = validated_data.get("available", instance.available)
        instance.pinned = validated_data.get("pinned", instance.pinned)
        
        instance.save()
        return instance
        
       
    
    
    def validate_name(self, value):
        unique =Accommodation.objects.filter(name=value)
        print(value)
        if unique.exists():
            raise serializers.ValidationError("house with the same title already exist")
        return value
