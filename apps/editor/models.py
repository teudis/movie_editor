from django.db import models
from django.utils.translation import gettext_lazy as _

from django.conf import settings

from apps.users.models import UserProfile

User = settings.AUTH_USER_MODEL


PROJECT_STATUS_CHOICES = (
    ('EDITING', _('EDITING')),
    ('WAITING', _('WAITING')),
    ('RENDERING', _('RENDERING')),
    ('FINISHED', _('FINISHED')),
)


# Create your models here.
class VideoProject(models.Model):
    title = models.CharField(_('title'), max_length=255)
    organization_uuid = models.UUIDField(_('organization identifier'))
    status = models.CharField(_('status'), max_length=10, choices=PROJECT_STATUS_CHOICES, default='EDITING')

    created_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='video_projects')
    created_date = models.DateTimeField(_('created'), auto_now_add=True)

    last_modified_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True, null=True, default=None)
    last_modified_date = models.DateTimeField(_('updated'), auto_now=True)

    class Meta:
        verbose_name = _('video project')
        verbose_name_plural = _('video projects')
        ordering = ('-created_date', )

    def __str__(self):
        return self.title


class Track(models.Model):
    project = models.ForeignKey(VideoProject, on_delete=models.CASCADE, related_name='time_line')
    name = models.CharField(_('name'), max_length=255, null=True, blank=True)
    position = models.PositiveIntegerField(_('position'))

    created_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='tracks')
    created_date = models.DateTimeField(_('created'), auto_now_add=True)

    last_modified_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    last_modified_date = models.DateTimeField(_('updated'), auto_now=True)

    def __str__(self):
        return f"{self.project} track: {self.position}"

    class Meta:
        verbose_name = _('track')
        verbose_name_plural = _('tracks')
        ordering = ('-position', )
        unique_together = ('project', 'position', )

#
#
# class Item(models.Model):
#     type = models.CharField(max_length=10)
#     track = models.ForeignKey(Track, on_delete=models.CASCADE, related_name='items')
#     timeline_start = models.PositiveIntegerField()
#
#     class Meta:
#         abstract = True
#
#
# class VideoMedia(models.Model):
#     file = models.FileField(upload_to='videos')
#
#
# class VideoItem(Item):
#     video_media = models.ForeignKey(VideoMedia, on_delete=models.CASCADE)
#
#     start = models.PositiveIntegerField()
#     length = models.PositiveIntegerField()
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.type = 'video'
