from django.contrib import admin
from .models import CharacterCard, Archetype, Rarity


# Register your models here.
@admin.register(Archetype)
class ArchetypeAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Archetype model
    """
    list_display = ("id", "literary_archetype", "archetype_traits")

@admin.action(description="Update rotation status")
def update_rotation_status(modeladmin, request, queryset):
    """
    Admin action to approve selected Fableseed instances.

    Sets the approval_status of the selected Fableseed objects to 1.
    """
    queryset.update(can_participate_in_rotation=0)

@admin.register(CharacterCard)
class CharacterCardAmin(admin.ModelAdmin):
    list_display = ("name", "archetype", "rarity", "can_participate_in_rotation")
    list_filter = ("archetype", "rarity",)
    actions = [update_rotation_status]

    search_fields = ["name"]
    
@admin.register(Rarity)
class RarityAdmin(admin.ModelAdmin):
    list_display = ("name", "level", "price")
    