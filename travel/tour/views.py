from django.shortcuts import render
from .serializers import TourClassSerializer, HotelSerializer, TravelSerializer
from .models import TourClass, Hotel, Travel
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request


class TravelView(APIView):
    
    def get(self, request, pk=None):
        if pk is None:
            travels = Travel.objects.all()
            serializer = TravelSerializer(travels, many=True)
            return Response({'travels': serializer.data, "detail": "All travels!"})
        try:
            travel = Travel.objects.get(pk=pk)
        except Travel.DoesNotExist:
            return Response({'detail': "Object does not exist!"})
        else:
            serializer = TravelSerializer(travel)
            return Response({'travel': serializer.data, "detail": "Travel detail."})
    
    def post(self, request):
        serializer = TravelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'travel': serializer.data, "detail": "A travel has been added successfully."})
    
    def put(self, request, pk=None):
        if pk is None:
            return Response({"detail": "A valid pk should be provided"})
        try: 
            travel = Travel.objects.get(pk=pk)
        except Travel.DoesNotExist:
            return Response({'detail': 'Object does not exist!'})
        else:
            serializer = TravelSerializer(instance=travel, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'new_travel': serializer.data, "detail": "A travel has been changed successfully!"})
        
    def delete(self, request, pk):
        if pk is None:
            return Response({"detail": "Method \"DELETE\" not allowed."})
        try:
            travel = Travel.objects.get(pk=pk)
        except Travel.DoesNotExist:
            return Response({'detail': "Object does not exist!"})
        else:
            travel.delete()
            return Response({"detail": "A travel has been successfully deleted."})
    

        
        
class TourClassView(APIView):
    
    def get(self, request, pk=None):
        if pk is None:
            tour_classes = TourClass.objects.all()
            serializer = TourClassSerializer(tour_classes, many=True)
            return Response({'tour_classes': serializer.data, "detail": "All tour classes!"})
        try:
            tour_class = TourClass.objects.get(pk=pk)
        except TourClass.DoesNotExist:
            return Response({'detail': "Object does not exist!"})
        else:
            serializer = TourClassSerializer(tour_class)
            return Response({'tour_class': serializer.data, "detail": "Tour class detail."})
    
    def post(self, request):
        serializer = TourClassSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'tour_class': serializer.data, "detail": "A tour class has been added successfully."})
    
    def put(self, request, pk=None):
        if pk is None:
            return Response({"detail": "A valid pk should be provided"})
        try: 
            tour_class = TourClass.objects.get(pk=pk)
        except TourClass.DoesNotExist:
            return Response({'detail': 'Object does not exist!'})
        else:
            serializer = TourClassSerializer(instance=tour_class, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'new_tour_class': serializer.data, "detail": "A tour class has been changed successfully!"})
        
    def delete(self, request, pk):
        if pk is None:
            return Response({"detail": "Method \"DELETE\" not allowed."})
        try:
            tour_class = TourClass.objects.get(pk=pk)
        except TourClass.DoesNotExist:
            return Response({'detail': "Object does not exist!"})
        else:
            tour_class.delete()
            return Response({"detail": "Tour class has been successfully deleted."})
    

class HotelView(APIView):
    
    def get(self, request, pk=None):
        if pk is None:
            hotels = Hotel.objects.all()
            serializer = HotelSerializer(hotels, many=True)
            return Response({'hotels': serializer.data, "detail": "All hotels!"})
        try:
            hotel = Hotel.objects.get(pk=pk)
        except Hotel.DoesNotExist:
            return Response({'detail': "Object does not exist!"})
        else:
            serializer = HotelSerializer(hotel)
            return Response({'hotel': serializer.data, "detail": "Hotel detail."})
    
    def post(self, request):
        serializer = HotelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'hotel': serializer.data, "detail": "A hotel has been added successfully."})
    
    def put(self, request, pk=None):
        if pk is None:
            return Response({"detail": "A valid pk should be provided"})
        try: 
            hotel = Hotel.objects.get(pk=pk)
        except Hotel.DoesNotExist:
            return Response({'detail': 'Object does not exist!'})
        else:
            serializer = HotelSerializer(instance=hotel, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'new_hotel': serializer.data, "detail": "A hotel has been changed successfully!"})
        
    def delete(self, request, pk):
        if pk is None:
            return Response({"detail": "Method \"DELETE\" not allowed."})
        try:
            hotel = Hotel.objects.get(pk=pk)
        except Hotel.DoesNotExist:
            return Response({'detail': "Object does not exist!"})
        else:
            hotel.delete()
            return Response({"detail": "A hotel has been successfully deleted."})
    
