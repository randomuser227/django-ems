from django.contrib import admin

from .models import *

admin.site.register(EventOrganiser)
admin.site.register(Customer)
admin.site.register(Events)
admin.site.register(Tickets)
admin.site.register(Bookings)
# admin.site.register(User)

