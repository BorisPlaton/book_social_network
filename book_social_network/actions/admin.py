from django.contrib import admin

from actions.models import Action


@admin.register(Action)
class ActionAdmin(admin.ModelAdmin):
    list_display = ('user', 'description', 'target', 'action_time')
    list_filter = ('action_time', 'description')
    search_fields = ('description',)
