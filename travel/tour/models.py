from django.db import models


class TourClass(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.name
    

class Hotel(models.Model):
    name = models.CharField(max_length=255)
    star_rating = models.IntegerField()
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.name
    


class Travel(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    period = models.IntegerField(default=3) # days
    price = models.DecimalField(max_digits=10, decimal_places=2)
    tour_class = models.ForeignKey(TourClass, on_delete=models.SET_NULL, null=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.SET_NULL, null=True)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.name