from django.contrib import admin
from core.models import TagPerk, Perk, Tag
from user.models import UserPerk


@admin.register(Perk)
class PerkAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ('name', )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ('name', )


@admin.register(TagPerk)
class TagPerkAdmin(admin.ModelAdmin):
    list_display = ['tag', 'perk', 'level']
