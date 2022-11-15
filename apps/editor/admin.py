from django.contrib import admin

# Register your models here.
from apps.editor.models import VideoProject, Track


@admin.register(VideoProject)
class VideoProjectAdmin(admin.ModelAdmin):
    list_filter = ('status', 'organization_uuid', )
    list_display = ('title', 'organization_uuid', 'status', )
    search_fields = ('title', )


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_filter = ('project', )
    list_display = ('__str__', 'position', 'project', 'name', 'created_by', )
