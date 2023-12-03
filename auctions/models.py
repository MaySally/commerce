from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

    def __str__(self):
        return f"{self.id}: {self.username} contact {self.email}"

class Listing(models.Model):
    listing_user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing_name = models.CharField(max_length=64)
    listing_description = models.TextField()
    listing_startprice = models.DecimalField(max_digits=1300000, decimal_places=2)

    def __str__(self):
        return f"{self.id}: {self.listing_name} listed by {self.listing_user} for ${self.listing_startprice}"