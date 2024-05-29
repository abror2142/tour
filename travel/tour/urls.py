from django.urls import path
from .views import TourClassView, HotelView, TravelView


urlpatterns = [
    path('travel/', TravelView.as_view()),
    path('travel/<int:pk>/', TravelView.as_view()),
    path('tour-class/', TourClassView.as_view()),
    path('tour-class/<int:pk>/', TourClassView.as_view()),
    path('hotel/', HotelView.as_view()),
    path('hotel/<int:pk>/', HotelView.as_view())
]
