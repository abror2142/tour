from django.urls import path
from .views import TravelDetailView, TravelListView, TourClassDetailView, TourClassListView, HotelDetailView, HotelListView


urlpatterns = [
    path('travel/', TravelListView.as_view()),
    path('travel/<int:pk>/', TravelDetailView.as_view()),
    path('tour-class/', TourClassListView.as_view()),
    path('tour-class/<int:pk>/', TourClassDetailView.as_view()),
    path('hotel/', HotelListView.as_view()),
    path('hotel/<int:pk>/', HotelDetailView.as_view())
]
