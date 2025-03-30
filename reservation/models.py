from django.db import models
from django.db import models
from django.contrib.auth.models import User

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    num_guests = models.IntegerField()

    def __str__(self):
        return f"Booking for {self.user.username} on {self.date} at {self.time}"
