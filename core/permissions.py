from rest_framework.permissions import BasePermission, SAFE_METHODS
from .models import *

class ReadOnly(BasePermission):

    def has_permission(self, request, view):
        return request.method in SAFE_METHODS
    

class AuthorOrReadOnly(BasePermission):
    def has_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        
        return request.user == obj.author
    

class EventOrgPermission(BasePermission):
    def has_permission(self, request, view):
        username = request.data.get("username")
        if EventOrganiser.objects.filter(name=username).exists():
            return True

        return False
    

class BookingsPermission(BasePermission):
    
    def has_permission(self, request, view):
        username = request.data.get("username")
        if Customer.objects.filter(name=username).exists():
            return True
        return False