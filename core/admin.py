from django.contrib import admin
from core.models import Perks, Tag


@admin.register(Perks)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ('name', )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ('name', )
