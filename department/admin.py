from django.contrib import admin
from department.models import Department


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_parent_name']

    def get_parent_name(self, obj):
        if obj.parent:
            return obj.parent.name
        return ''
    get_parent_name.short_description = 'Родитель'
