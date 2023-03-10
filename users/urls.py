from django.urls import path
from . import views


urlpatterns = [
    path("user/sign-in/", views.UserCreationView.as_view()),
    
    path("user/profile/", views.UserProfileView.as_view())
]