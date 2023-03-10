from django.urls import path

from .views import AccommodatioFilterView, AccommodationMutateView, AccommodationListView, CategoryListView, LocationListView

urlpatterns = [
    # UNAUTHENTICATED VIEWS
    path("", AccommodationListView.as_view(), name="accommodation-list"),
    path("detail/<slug:slug>/", AccommodationListView.as_view(), name="accommodation-detail"),
    
    # FILTER VIEWS
    path("search/<str:params>/", AccommodatioFilterView.as_view(), name="accommodation-search"),
    path("filter/categories/<str:category>/", AccommodatioFilterView.as_view(), name="accommodation-category-filter"),
    path("filter/locations/<str:location>/", AccommodatioFilterView.as_view(), name="accommodation-location-filter"),
    path("filter/categories/<str:category>/locations/<str:location>/", AccommodatioFilterView.as_view(), name="accommodation-category-location-filter"),
    
    # CATEGORIES AND LOCATIONS LIST VIEWS
    path("categories/", CategoryListView.as_view(),name="category-list" ),
    path("locations/", LocationListView.as_view(),name="location-list" ),
    
    
    #AUTHENTICATION REQUIRED |  CRUD VIEWS
    path("mutate/", AccommodationMutateView.as_view()),
    path("mutate/<str:slug>/", AccommodationMutateView.as_view(), ),
]
