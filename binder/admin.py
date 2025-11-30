from django.contrib import admin
from .models import Usercards

# Register your models here.
@admin.register(Usercards)
class UserCardsAdmin(admin.ModelAdmin):
    list_display = ("id", "owner", "character_name", "order_reference", "date_purchased", "purchase_price")