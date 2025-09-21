from django.db import models

# Create your models here.

from django.db import models
import uuid
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
  
class Listing(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    host = models.ForeignKey(User,on_delete=models.CASCADE, related_name='host')
    name = models.CharField(max_length=128)
    description = models.TextField()
    location = models.CharField(max_length=128)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    city = models.CharField(max_length=128)
    country = models.CharField(max_length=128)
    created_at = models.DateTimeField(default=timezone.now)
    updateted_at = models.DateTimeField(default=timezone.now)

    

    def __str__(self):
        return f'{self.host.username} owned {self.name}'
    
class Booking(models.Model):

    STATUS = [('pending','Pending'),
              ('confrimed', 'Confirmed'),
              ('canceled', 'Canceled')]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="lodge")
    guest = models.ForeignKey(User, on_delete=models.CASCADE, related_name="guest")
    check_in = models.DateTimeField(default=timezone.now)
    check_out = models.DateField(default=timezone.now)
    total_price = models.DecimalField(max_digits=6, decimal_places=2)
    status = models.CharField(choices=STATUS, default=STATUS[0][0], max_length=12)
    created_at = models.DateTimeField(default=timezone.now)


    

    def __str__(self):
        return f'{self.guest.username} books {self.listing.name}'

class Review(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    property = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="property")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_review")
    rating = models.IntegerField(default=3, validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_at = models.DateTimeField(default=timezone.now)
    

    def __str__(self):
        return f'{self.user.username} reviewed {self.property.name} with {self.rating}' 


class Payment(models.Model):
    STATUS = [('pending','Pending'),
              ('completed', 'Completed'),
              ('cancel','Canceld'),
              ('failed','Failed')]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_payment")
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name="booking")
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    status = models.CharField(choices=STATUS, default=STATUS[0][0], max_length=16)

    def __str__(self):
        return f'{self.user.username} paid {self.amount}'