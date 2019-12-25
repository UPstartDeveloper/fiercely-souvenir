from django.db import models
from django.contrib.auth.models import User
from travelly import settings
from django.urls import reverse
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)

    def __str__(self):
        '''Return the related User's username.'''
        return f"{self.user.username}'s Profile"
