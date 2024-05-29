from rest_framework import serializers
from .models import TourClass, Hotel, Travel

class TourClassSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=25)
    description = serializers.CharField()
    added_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    
    def create(self, validated_data):
        return TourClass.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance
    
    
class HotelSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    description = serializers.CharField()
    star_rating = serializers.IntegerField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    added_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    
    def create(self, validated_data):
        return Hotel.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.star_rating = validated_data.get('star_rating', instance.star_rating)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance
    

class TravelSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    description = serializers.CharField()
    period = serializers.IntegerField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    tour_class_id = serializers.IntegerField()
    hotel_id = serializers.IntegerField()
    added_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    
    def create(self, validated_data):
        return Travel.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.period = validated_data.get('period', instance.period)
        instance.price = validated_data.get('price', instance.price)
        instance.tour_class_id  = validated_data.get('tour_class_id', instance.tour_class_id)
        instance.hotel_id = validated_data.get('hotel_id', instance.hotel_id)
        instance.save()
        return instance
    