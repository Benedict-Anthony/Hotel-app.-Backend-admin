from django.urls import path

from .views import AccommodationMutateView, AccommodationListView, CategoryListView

urlpatterns = [
    path("mutate/", AccommodationMutateView.as_view()),
    path("", AccommodationListView.as_view(), name="accommodation-list"),
    path("categories/", CategoryListView.as_view(), ),
    
    path("<slug:slug>/", AccommodationListView.as_view()),
    
    path("mutate/<str:id>/", AccommodationMutateView.as_view(), ),
]
