from django.contrib import admin
from burgers.models import *

# Register your models here.
@admin.register(Burger)
class BurgerAdmin(admin.ModelAdmin):
    pass
