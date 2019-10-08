from django.db import models
    
class User(models.Model):
    firstName   = models.CharField(max_length=255)
    lastName    = models.CharField(max_length=255)
    email       = models.CharField(max_length=255)
    age         = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"User: First: {self.firstName}, Last:{self.lastName}, Email:{self.email}, Age:{self.age}"