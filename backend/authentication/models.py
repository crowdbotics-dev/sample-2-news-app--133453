from django.conf import settings
from django.db import models


class User(models.Model):
    "Generated Model"
    username = models.CharField(
        max_length=150,
        null=False,
        blank=False,
    )
    email = models.EmailField(
        null=False,
        blank=False,
    )
    password = models.CharField(
        max_length=255,
        null=False,
        blank=False,
    )
    accepted_privacy_agreement = models.BooleanField(
        null=False,
        blank=False,
    )

    def get_absolute_url(self):
        return reverse("authentication:detail", kwargs={"username": self.username})


# Create your models here.
