from django.db import models
from django.db.models import Q
from users.models import CustomUser
from django.utils.text import slugify
from PIL import Image
import secrets
from io import BytesIO
from django.core.files import File

def customId():
    return secrets.token_hex(6)



class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name


class Images(models.Model):
    id = models.CharField(max_length=20, primary_key=True, default=customId, editable=False)
    image = models.ImageField(upload_to="accommodation_images")
    thumbnail = models.ImageField(upload_to="accommodation_images", null=True, blank=True)
        
    def image_url(self):
        try:
            return f'https://hostelapi.onrender.com{self.image.url}'
        except:
            return ""
    
    def image_thumbnail(self):
       if self.image:
           self.thumbnail = self.make_thumbnail(image=self.image)
           self.save()
           return f'https://hostelapi.onrender.com{self.thumbnail.url}'
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
    
    def search(self, params):
        lookup_params = Q(name__icontains=params) | Q(description__icontains=params) | Q(distance__icontains=params) | Q(category__name__icontains=params) | Q(location__name__icontains=params)
        return self.get_queryset().filter(lookup_params)

class Accommodation(models.Model):
    id = models.CharField(max_length=20, primary_key=True, default=customId, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    distance = models.CharField(max_length=255)
    price = models.FloatField()
    agent = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    _rating = models.ManyToManyField(CustomUser, related_name="accommodation_rating")
    banner = models.ImageField(upload_to="accommodation_images", null=True, blank=True)
    images = models.ManyToManyField(Images, related_name="accommodation_images")
    available = models.BooleanField(default=True)
    pinned = models.BooleanField(default=False)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    

    objects = models.Manager()
    accomodation = AccommodationManager()
    
    
    def __str__(self):
        return f"{self.category} - {self.distance} - {self.price}"
    
    
    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.name}-{self.id}")
        return super().save(args, kwargs)
    
    
    def banner_url(self):
        try:
            return f'https://hostelapi.onrender.com{self.banner.url}'
        except:
            return ""
 