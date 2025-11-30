"""
Admin configuration for the core app models.

This module customises the Django admin interface for the core
models CharacterCard, Archetype, and Rarity. It provides:

- Inline display options and list views for each model.
- Filtering and search capabilities to improve usability.
- Custom admin actions, such as updating the rotation status
  of characters, to streamline administrative workflows.
"""
from django.contrib import admin
from .models import CharacterCard, Archetype, Rarity


# Register your models here.
@admin.register(Archetype)
class ArchetypeAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Archetype model
    """
    list_display = ("id", "literary_archetype", "archetype_traits")


@admin.action(description="Take out of rotation")
def rotation_false(modeladmin, request, queryset):
    """
    Admin action to approve selected Fableseed instances.
    Sets the approval_status of the selected Fableseed objects to 0.
    """
    queryset.update(can_participate_in_rotation=0)


@admin.action(description="Put into rotation")
def rotation_true(modeladmin, request, queryset):
    """
    Admin action to approve selected Fableseed instances.
    Sets the approval_status of the selected Fableseed objects to 1.
    """
    queryset.update(can_participate_in_rotation=1)


@admin.register(CharacterCard)
class CharacterCardAmin(admin.ModelAdmin):
    list_display = (
        "legend_id",
        "name",
        "archetype",
        "rarity",
        "can_participate_in_rotation"
    )
    list_filter = ("archetype", "rarity",)
    actions = [rotation_false, rotation_true]
    search_fields = ["name"]


@admin.register(Rarity)
class RarityAdmin(admin.ModelAdmin):
    list_display = ("name", "level", "price")
