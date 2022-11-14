from django.contrib import admin

# Register your models here.
from editor.models import VideoProject


@admin.register(VideoProject)
class ChatConfigAdmin(admin.ModelAdmin):
    pass
