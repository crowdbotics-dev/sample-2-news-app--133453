from django.conf import settings
from django.db import models


class ContentModeration(models.Model):
    "Generated Model"
    article = models.ForeignKey(
        "news.Article",
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name="contentmoderation_article",
    )
    action = models.CharField(
        max_length=100,
    )
    timestamp = models.DateTimeField(
        null=False,
        blank=False,
    )


class UserManagement(models.Model):
    "Generated Model"
    user = models.ForeignKey(
        "authentication.User",
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name="usermanagement_user",
    )
    action = models.CharField(
        max_length=100,
    )
    timestamp = models.DateTimeField(
        null=False,
        blank=False,
    )


# Create your models here.
