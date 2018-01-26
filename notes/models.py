from django.conf import settings
from django.db import models


class Note(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField(null=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='notes',
        on_delete=models.CASCADE,
    )
