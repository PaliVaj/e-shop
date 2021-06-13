from django.contrib import admin

# Register your models here.
from viewer.models import Brand, Fuel, Transmission, Product

admin.site.register(Brand)
admin.site.register(Fuel)
admin.site.register(Transmission)
admin.site.register(Product)