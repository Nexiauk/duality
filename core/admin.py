from django.contrib import admin
from .models import CharacterCard, Archetype, Rarity


# Register your models here.
@admin.register(Archetype)
class ArchetypeAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Archetype model
    """
    list_display = ("id", "literary_archetype", "archetype_traits")

@admin.register(CharacterCard)
class CharacterCardAmin(admin.ModelAdmin):
    list_display = ("id", "name", "archetype", "rarity", "can_participate_in_rotation")
    list_filter = ("archetype",)


    