from django.contrib import admin
from .models import ShopScheduler, ShopScheduleItems

# Register your models here.

@admin.register(ShopScheduler)
class ShopSchedulerAdmin(admin.ModelAdmin):
    list_display = (
        "start_time",
        "end_time",
        "rotation_type")

@admin.register(ShopScheduleItems)
class ShopScheduleItemsAdmin(admin.ModelAdmin):
    list_display = ("shop_scheduler",
                    "character",
                    "sale_price"
                    )