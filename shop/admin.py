from django.contrib import admin
from shop.models import ShopScheduler, ShopScheduleItems


class ShopScheduleItemsInline(admin.TabularInline):
    model = ShopScheduleItems
    extra = 12

@admin.register(ShopScheduler)
class ShopSchedulerAdmin(admin.ModelAdmin):
    inlines = [ShopScheduleItemsInline]
    list_display = (
        "start_time",
        "end_time",
        "rotation_type",
        'allocated_characters'
        )
    def allocated_characters(self, obj):
        names = sorted(item.character.name for item in obj.shopscheduleitems_set.all())
        return ", ".join(names)

