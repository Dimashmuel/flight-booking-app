from django.contrib import admin
from .models import Flight, Booking

# Register the Flight model so it appears in the Django admin interface
admin.site.register(Flight)

# Register the Booking model so it appears in the Django admin interface
admin.site.register(Booking)
