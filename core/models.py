from django.db import models
from datetime import date
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# from django.contrib.auth.models import User
# from .tasks import *
# from .tasks import send_email
from .tasks import send_email, test


# class User(AbstractUser):
#     ROLE_CHOICES = (
#         ('event_organiser', 'EventOrganiser'),
#         ('customer', 'Customer')
#     )

#     role = models.CharField(max_length=15, choices= ROLE_CHOICES)
    # is_organiser = models.BooleanField('Is organiser', default= False)
    # is_customer = models.BooleanField('Is customer', default= False)

class EventOrganiser(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, default='')
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
    
class Customer(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, default='')
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class Events(models.Model):
    organiser = models.ForeignKey(EventOrganiser, on_delete=models.CASCADE)
    name =models.CharField(max_length=200)
    event_date = models.DateField(default=date.today)
    venue = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name

class Tickets(models.Model):
    event = models.ForeignKey(Events, on_delete=models.CASCADE)
    ticket_type = models.CharField(max_length=50)
    price = models.IntegerField()
    available = models.IntegerField()

    def __str__(self) -> str:
        return self.ticket_type
    

class Bookings(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    event = models.ForeignKey(Events, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Tickets, on_delete=models.CASCADE) #check later
    

    # def __str__(self) -> str:
    #     return self.name




@receiver(post_save, sender=Bookings)
def booking_done(sender, instance, **kwargs):
    print("Booking Done")
    print(sender, instance, kwargs)
    try:
        send_email.delay()
        print("no error -----------")
    except Exception as e:
        print(e, "----------")
    
    # test.delay()
    
    print("email sent from signal")

