from django.contrib import admin
from .models import users, device, calculation_of_carbon_footprint, treek
# Register your models here.
admin.site.register(users)
admin.site.register(device)
admin.site.register(calculation_of_carbon_footprint)
admin.site.register(treek)