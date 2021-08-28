from django.contrib import admin
from core.models import Perks, Tags


@admin.register(Perks)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ('name', )


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ('name', )
