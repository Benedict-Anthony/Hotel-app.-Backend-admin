from django.db import models
from users.models import CustomUser
from django.utils.text import slugify
from PIL import Image
import secrets
from io import BytesIO
from django.core.files import File

from datetime import datetime

def customId():
    return secrets.token_hex(10)


class AccommodationCategory(models.Model):
    category = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    
    class Meta:
        verbose_name_plural = "Accommodation Categories"
    
    
    def __str__(self):
        return self.category

class Location(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name


class AccommodationImages(models.Model):
    image = models.ImageField(upload_to="accommodation_images", null=True, blank=True)
    thumbnail = models.ImageField(upload_to="accommodation_images", null=True, blank=True)
    class Meta:
        verbose_name_plural = "Accommodation Images"
    
    def image_thumbnail(self):
       if self.image:
           self.thumbnail = self.make_thumbnail(image=self.image)
           self.save()
           return self.thumbnail.url
       return ""
           
    def make_thumbnail(self, image):
        img = Image.open(image)
        img.convert("RGB")
        img.thumbnail(size=(300, 300))
        
        thumb_io = BytesIO()
        img.save(thumb_io, "PNG", quality=85)
        
        thumbnail = File(thumb_io, name=image.name)
        return thumbnail
    

class AccommodationManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(available=True)

class AccommodationSpace(models.Model):
    id = models.CharField(max_length=20, primary_key=True, default=customId, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    category = models.ForeignKey(AccommodationCategory, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    distance = models.CharField(max_length=255)
    price = models.FloatField()
    agent = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    _rating = models.ManyToManyField(CustomUser, related_name="accommodation_rating")
    banner = models.ImageField(upload_to="accommodation_images", null=True, blank=True)
    images = models.ManyToManyField(AccommodationImages, related_name="accommodation_images")
    available = models.BooleanField(default=True)
    pinned = models.BooleanField(default=False)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    

    objects = models.Manager()
    accomodation = AccommodationManager()
    
    class Meta:
        verbose_name_plural = "Accommodation Spaces"
    
    def __str__(self):
        return f"{self.category} - {self.distance} - {self.price}"
    
    
    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.name}-{self.id}")
        return super().save(args, kwargs)
 