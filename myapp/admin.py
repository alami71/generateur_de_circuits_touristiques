from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *
#admin.site.register(Actualite)
#admin.site.register(Artisanat)
#admin.site.register(Chambre)
admin.site.register(CircuitVoyage)
admin.site.register(Client)
admin.site.register(Destination)
admin.site.register(Hotel)
#admin.site.register(Materiels)
#admin.site.register(Messages)
admin.site.register(Moussem)
admin.site.register(Plat)
#admin.site.register(Reservation)
admin.site.register(Restaurant)
admin.site.register(Ville)

