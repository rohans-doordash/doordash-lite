from django.contrib import admin
from .models import Customer
from .models import FoodItem
from .models import Order

# Register your models here.
admin.site.register(Customer)
admin.site.register(FoodItem)
admin.site.register(Order)
