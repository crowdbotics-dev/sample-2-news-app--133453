from django.conf import settings
from django.db import models


class UserProfile(models.Model):
    "Generated Model"
    user = models.OneToOneField(
        "authentication.User",
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name="userprofile_user",
    )
    selected_categories = models.ManyToManyField(
        "news.Category",
        related_name="userprofile_selected_categories",
    )
    saved_articles = models.ManyToManyField(
        "news.Article",
        related_name="userprofile_saved_articles",
    )


# Create your models here.
