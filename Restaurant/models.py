from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guest = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(6)
        ]
    )
    booking_date = models.DateTimeField()
    def __str__(self):
        return(self.name)

class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()

    def __str__(self):
        return(self.title)


