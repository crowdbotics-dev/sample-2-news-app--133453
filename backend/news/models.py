from django.conf import settings
from django.db import models


class Category(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=100,
    )


class Topic(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=100,
    )
    category = models.ForeignKey(
        "news.Category",
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name="topic_category",
    )


class Article(models.Model):
    "Generated Model"
    title = models.CharField(
        max_length=255,
    )
    content = models.TextField()
    category = models.ForeignKey(
        "news.Category",
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name="article_category",
    )
    topics = models.ManyToManyField(
        "news.Topic",
        related_name="article_topics",
    )


# Create your models here.
