from django.contrib import admin
from shop.models import ShopScheduler, ShopScheduleItems
from core.models import CharacterCard


class ShopScheduleItemsInline(admin.TabularInline):
    model = ShopScheduleItems
    extra = 12

    def formfield_for_foreignkey(self, db_field, request, *args, **kwargs):
        if db_field.name == "character":
            kwargs["queryset"] = CharacterCard.objects.filter(can_participate_in_rotation=True)
            return super().formfield_for_foreignkey(db_field, request, **kwargs)

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
        names = sorted(item.character.name for item in obj.scheduled_items.all())
        return ", ".join(names)

