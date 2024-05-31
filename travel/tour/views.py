from django.shortcuts import render
from .serializers import TourClassSerializer, HotelSerializer, TravelSerializer
from .models import TourClass, Hotel, Travel
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import generics
from rest_framework import mixins


class TravelListView(mixins.ListModelMixin, 
                 mixins.CreateModelMixin,
                 generics.GenericAPIView):
    queryset = Travel.objects.all()
    serializer_class = TravelSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

class TravelDetailView(mixins.RetrieveModelMixin, 
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 generics.GenericAPIView): 
    queryset = Travel.objects.all()
    serializer_class = TravelSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
    
class TourClassListView(mixins.ListModelMixin, 
                 mixins.CreateModelMixin,
                 generics.GenericAPIView):
    queryset = TourClass.objects.all()
    serializer_class = TourClassSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

class TourClassDetailView(mixins.RetrieveModelMixin, 
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 generics.GenericAPIView): 
    queryset = TourClass.objects.all()
    serializer_class = TourClassSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class HotelListView(mixins.ListModelMixin, 
                 mixins.CreateModelMixin,
                 generics.GenericAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

class HotelDetailView(mixins.RetrieveModelMixin, 
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 generics.GenericAPIView): 
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)