from django.contrib import admin
from .models import Customer
from .models import FoodItem
from .models import Order
from .models import Restaurant
from .models import Menu

# Register your models here.
admin.site.register(Customer)
admin.site.register(FoodItem)
admin.site.register(Order)
admin.site.register(Restaurant)
admin.site.register(Menu)
