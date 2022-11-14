from django.db import models

from django.conf import settings
User = settings.AUTH_USER_MODEL


PROJECT_STATUS_CHOICES = (
    ('EDITING', 'EDITING'),
    ('WAITING', 'WAITING'),
    ('RENDERING', 'RENDERING'),
    ('FINISHED', 'FINISHED'),
)


# Create your models here.
class VideoProject(models.Model):
    title = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=PROJECT_STATUS_CHOICES)
    organization_uuid = models.UUIDField()

    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creator')
    created_date = models.DateTimeField('creation date', auto_now_add=True)

    last_modified_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='last_modified_by')
    last_modified_date = models.DateTimeField('creation date', auto_now=True)

# class Track(models.Model):
#     project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='time_line')
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
