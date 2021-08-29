from django.contrib import admin

from user.models import User, UserPerk


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['get_full_name', 'department', 'get_tasks_num', 'kpi']

    def get_full_name(self, obj):
        if obj.first_name or obj.last_name:
            return f'{obj.last_name} {obj.first_name}'
        else:
            return '-'
    get_full_name.short_description = 'Имя'

    def get_tasks_num(self, obj):
        if obj.tasks:
            return obj.tasks.count()
        return 0
    get_tasks_num.short_description = 'Кол-во задач'


@admin.register(UserPerk)
class UserPerkAdmin(admin.ModelAdmin):
    list_display = ['user', 'perk', 'level']
