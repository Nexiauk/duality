from django.contrib import admin
from .models import CharacterCard, Archetype, Rarity

# Register your models here.
@admin.register(Archetype)
class ArchetypeAdmin(admin.ModelAdmin):
    list_display = ("literary_archetype", "archetype_traits")
    