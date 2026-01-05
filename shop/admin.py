"""
Admin configuration for the shop app.

This module customises how shop schedules and their related items
are managed through the Django admin interface. It enables inline
allocation of schedule items within each shop schedule and filters the
available character list to only include those eligible for rotation.
"""

from django.contrib import admin
from shop.models import ShopScheduler, ShopScheduleItems
from core.models import CharacterCard


class ShopScheduleItemsInline(admin.TabularInline):
    """
    Inline configuration for ShopScheduleItems.
    Allows allocating of shop items to the schedule
    directly within the ShopScheduler admin page.
    """
    model = ShopScheduleItems
    extra = 0
    autocomplete_fields = ['character']

    def formfield_for_foreignkey(self, db_field, request, *args, **kwargs):
        """
        Restricts the character dropdown list in the inline form
        to only show characters eligible for shop rotation.
        """
        if db_field.name == "character":
            kwargs["queryset"] = CharacterCard.objects.filter(
                can_participate_in_rotation=True
            )
            return super().formfield_for_foreignkey(
                db_field, request, **kwargs
            )


@admin.register(ShopScheduler)
class ShopSchedulerAdmin(admin.ModelAdmin):
    """
    Custom admin configuration for ShopScheduler.
    Displays related schedule items inline and provides
    a readable list of allocated characters.
    """
    inlines = [ShopScheduleItemsInline]
    autocomplete_fields = ['characters']
    list_display = (
        "start_time",
        "end_time",
        "rotation_type",
        'allocated_characters'
    )

    def allocated_characters(self, obj):
        """
        Returns a comma-separated list of character names
        linked to this schedule, sorted alphabetically.
        This allows admin to see at a glance which characters are
        assigned to the shop schedule.
        """
        names = sorted(
            item.character.name for item in obj.scheduled_items.all())
        return ", ".join(names)
