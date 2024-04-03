from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from rest_framework import status

from .serializers import *
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from .permissions import *




# class UserRegistrationView(APIView):
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EventsAPI(APIView):

    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [EventOrgPermission]
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        event_objs = Events.objects.all()
        serializer = EventSerializer(event_objs, many=True)
        return Response({'status':status.HTTP_200_OK, 'payload': serializer.data, 'message': 'Returned Event details'})



    def post(self, request):
        serializer = EventSerializer(data=request.data)
        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'status': status.HTTP_400_BAD_REQUEST, 'errors': serializer.errors, 'message': 'Event creation failed'})
        serializer.save()

        return Response({'status':200, 'payload': serializer.data, 'message': 'New Event created'})

    def patch(self, request):
        print("-----",request.data['id'], type(request.data))
        try:
            print("-----",request.data['id'])
            event_obj = Events.objects.get(id=request.data['id'])
            data = request.data
            print("------------",data)
            serializer = EventSerializer(event_obj, data=request.data, partial =True)
            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'status':403, 'errors':serializer.errors,'message':'Something went wrong'})
            serializer.save()
            return Response({'status':200, 'payload':serializer.data,'message':'Updated'})
        except Exception as e:
            return Response({'status':403,'message':'invalid data' })

    def delete(self, request):
        print("----", request.data.get('id'), type(request.data))
        id = request.data.get('id')
        obj = Events.objects.get(pk=id)
        obj.delete()
        return Response({'status':200, 'message': ' Event Deleted'})


class BookingsAPI(APIView):

    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [BookingsPermission]

    def get(self, request):
        booking_objs = Bookings.objects.all()
        serializer = BookingSerializer(booking_objs, many=True)
        return Response({'status':200, 'payload':serializer.data, 'message':'booking data'})


    def post(self, request):
        serializer = BookingSerializer(data=request.data)
        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'status':403, 'errors': serializer.errors, 'message': 'Booking failed'})
        serializer.save()

        return Response({'status':200, 'payload': serializer.data, 'message': 'New Booking created'})

    def patch(self, request):
        try:
            booking_obj = Bookings.objects.get(id=request.data['id'])
            data = request.data
            serializer = BookingSerializer(booking_obj, data=request.data, partial =True)
            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'status':403, 'errors':serializer.errors,'message':'Something went wrong'})
            serializer.save()
            return Response({'status':200, 'payload':serializer.data,'message':'Updated'})
        except Exception as e:
            return Response({'status':403,'message':'invalid data' })

    def delete(self, request):
        id = request.data.get('id')
        obj = Bookings.objects.get(pk=id)
        obj.delete()
        return Response({'status':200, 'message': ' Booking Deleted'})
    

class EventOrganiserAPI(APIView):

    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [EventOrgPermission]

    def get(self, request):
        eventorg_objs = EventOrganiser.objects.all()
        serializer = EventOrganiserSerializer(eventorg_objs, many=True)
        return Response({'status':200, 'payload': serializer.data, 'message': 'Returned Event details'})



    def post(self, request):
        serializer = EventOrganiserSerializer(data=request.data)
        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'status':403, 'errors': serializer.errors, 'message': 'Event organiser creation failed'})
        serializer.save()

        return Response({'status':200, 'payload': serializer.data, 'message': 'New organiser created'})

    def patch(self, request):
        try:
            #give id in query parameter
            eventorg_obj = EventOrganiser.objects.get(id=request.data['id'])
            data = request.data
            serializer = EventOrganiserSerializer(eventorg_obj, data=request.data, partial =True)
            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'status':403, 'errors':serializer.errors,'message':'Something went wrong'})
            serializer.save()
            return Response({'status':200, 'payload':serializer.data,'message':'Updated'})
        except Exception as e:
            return Response({'status':403,'message':'invalid data' })

    def delete(self, request):
        #give id in json
        id = request.GET.get('id')
        obj = EventOrganiser.objects.get(pk=id)
        obj.delete()
        return Response({'status':200, 'message': ' Event Deleted'})
    
class CustomerAPI(APIView):

    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [EventOrgPermission]

    def get(self, request):
        customer_objs = Customer.objects.all()
        serializer = CustomerSerializer(customer_objs, many=True)
        return Response({'status':200, 'payload': serializer.data, 'message': 'Returned customer details'})



    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'status':403, 'errors': serializer.errors, 'message': 'Event organiser creation failed'})
        serializer.save()

        return Response({'status':200, 'payload': serializer.data, 'message': 'New customer created'})

    def patch(self, request):
        try:
            #give id in query parameter
            customer_obj = Customer.objects.get(id=request.data['id'])
            data = request.data
            serializer = CustomerSerializer(customer_obj, data=request.data, partial =True)
            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'status':403, 'errors':serializer.errors,'message':'Something went wrong'})
            serializer.save()
            return Response({'status':200, 'payload':serializer.data,'message':'Updated'})
        except Exception as e:
            print("error----", e)
            return Response({'status':403,'message':'invalid data'})

    def delete(self, request):
        #give id in json
        id = request.data.get('id')
        obj = Customer.objects.get(pk=id)
        obj.delete()
        return Response({'status':200, 'message': ' customer Deleted'})
    
class TicketAPI(APIView):

    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [EventOrgPermission]

    def get(self, request):
        ticket_objs = Tickets.objects.all()
        serializer = TicketsSerializer(ticket_objs, many=True)
        return Response({'status':200, 'payload': serializer.data, 'message': 'Returned ticket details'})



    def post(self, request):
        serializer = TicketsSerializer(data=request.data)
        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'status':403, 'errors': serializer.errors, 'message': 'ticket organiser creation failed'})
        serializer.save()

        return Response({'status':200, 'payload': serializer.data, 'message': 'New ticket created'})

    def patch(self, request):
        try:
            #give id in query parameter
            ticket_obj = Tickets.objects.get(id=request.data['id'])
            data = request.data
            serializer = TicketsSerializer(ticket_obj, data=request.data, partial =True)
            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'status':403, 'errors':serializer.errors,'message':'Something went wrong'})
            serializer.save()
            return Response({'status':200, 'payload':serializer.data,'message':'Updated'})
        except Exception as e:
            return Response({'status':403,'message':'invalid data' })

    def delete(self, request):
        #give id in json
        id = request.data.get('id')
        obj = Tickets.objects.get(pk=id)
        obj.delete()
        return Response({'status':200, 'message': ' Ticket Deleted'})

