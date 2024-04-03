from rest_framework import serializers
from .models import *



# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields =['username', 'email', 'role', 'password']
#         extra_kwargs = {'password': {'write_only': True}}
    
#     def create(self, validated_data):
#         user = User.objects.create_user(**validated_data)
#         return user


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class EventOrganiserSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventOrganiser
        fields = '__all__'
        # fields = ['name']


class EventSerializer(serializers.ModelSerializer):
    organiser = EventOrganiserSerializer
    class Meta:
        model = Events
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookings
        fields = '__all__'



class TicketsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tickets
        fields = '__all__'