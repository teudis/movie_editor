from django.conf import settings
from django.db import models

from django.utils.translation import gettext as _


EXTERNAL_USERS_CHOICES = (
    ('SYSTEM', _('System users')),  # users with accounts in external API
    ('PARTICIPANT', _('Participant users')),  # users logged with email in external API
)


class UserProfile(models.Model):
    """
    User model for profile users.
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    screen_name = models.CharField(_('screen name'), max_length=255)

    def __str__(self):
        return self.user.__str__()
