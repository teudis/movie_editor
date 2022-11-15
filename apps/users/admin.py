from django.contrib import admin

from apps.users import models

# Register your models here.
from apps.users.models import InteractionUser


@admin.register(InteractionUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user', 'screen_name', 'type')
