from django.contrib import admin

from images.models import Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'created', 'total_likes']
    list_filter = ['created', 'title']
    readonly_fields = ['total_likes']

    def total_likes(self, obj):
        return obj.user_likes.count()
