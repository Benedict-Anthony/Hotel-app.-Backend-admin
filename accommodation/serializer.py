from rest_framework import serializers

from accommodation.models import AccommodationCategory, AccommodationImages, AccommodationSpace
from users.models import CustomUser



class AccommodationCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = AccommodationCategory
        fields = [
            "id",
            "category",
        ]
        
class AccommodationAgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "name",
            "phone",
            "email",
        ]
        
class AccommodationImagesSerializer(serializers.ModelSerializer):
    thumbnail = serializers.SerializerMethodField()
    class Meta:
        model = AccommodationImages
        fields = [
            "image",
            "thumbnail"
        ]
        
    def get_thumbnail(self, obj):
        return obj.image_thumbnail()
        

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccommodationSpace
        fields = [
            "name",
        ]

class AccommodationSpaceSerializer(serializers.ModelSerializer):
    
    rating = serializers.SerializerMethodField()
    category = AccommodationCategorySerializer()
    location = LocationSerializer()
    
    class Meta:
        model = AccommodationSpace
        fields = [
            "id",
            "name",
            "category",
            "location",
            "distance",
            "price",
            "banner",
            "rating",
            "available",
            "pinned",
            "created_at",
            "updated_at",
            "slug"
            
        ]
        
    def get_rating(self, obj):
        return obj._rating.count()
    
    # def get_thumbnail(self, obj):
    #     return obj.thumbnail()
        

class AccommodationSpaceDetailSerializer(serializers.ModelSerializer):
    images = AccommodationImagesSerializer(many=True)
    rating = serializers.SerializerMethodField()
    category = AccommodationCategorySerializer()
    agent = AccommodationAgentSerializer()
    location = LocationSerializer()
        
    class Meta:
        model = AccommodationSpace
        fields = [
            "id",
            "category",
            "distance",
            "location",
            "description",
            "price",
            "agent",
            "rating",
            "images",
            "created_at",
            "updated_at",
            "available",
            "pinned"
        ]
        
    def get_rating(self, obj):
        return obj._rating.count()
    
    
    
    


class AccommodationCreateSerializer(serializers.ModelSerializer):
    images = AccommodationImagesSerializer(many=True)
    class Meta:
        model = AccommodationSpace
        fields = [
            "id",
            "name",
            "category",
            "distance",
            "location",
            "description",
            "banner",
            "price",
            "agent",
            "images",
            "slug",
            "available",
            "pinned"
        ]
        
    def create(self, validated_data):
        images_data = validated_data.pop("images")
        accommodation = AccommodationSpace.objects.create(**validated_data)
        for img in images_data:
            image = AccommodationImages.objects.create(**img)
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
        images = AccommodationImages.objects.get(id=instance.images.id)
        
        for img in images:
            instance.images.add(img)
            instance.save()
        return instance
        
       
    
    def validate_slug(self, value):
        unique =AccommodationSpace.objects.filter(slug=value)
        print(value)
        if unique.exists():
            raise serializers.ValidationError("house with the same title already exist")

        return value
    
    def validate_name(self, value):
        unique =AccommodationSpace.objects.filter(name=value)
        print(value)
        if unique.exists():
            raise serializers.ValidationError("house with the same title already exist")
        return value
