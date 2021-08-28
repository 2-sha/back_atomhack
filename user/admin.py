from django.contrib import admin

from user.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['get_full_name', 'department', 'kpi']

    def get_full_name(self, obj):
        if obj.first_name or obj.last_name:
            return f'{obj.last_name} {obj.first_name}'
        else:
            return '-'
    get_full_name.short_description = 'Имя'
