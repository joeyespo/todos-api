from django.contrib import admin

from .models import Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': [
        'id', 'created_at', 'updated_at', 'text', 'completed',
    ]})]
    readonly_fields = ['id', 'created_at', 'updated_at']
    search_fields = ['id', 'text']
    list_display = ['id', 'text', 'completed']
    list_filter = ['completed']
