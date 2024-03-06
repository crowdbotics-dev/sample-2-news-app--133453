from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    CategoryViewSet,
    TopicViewSet,
    ArticleViewSet,
    ArticleViewSet,
    CategoryViewSet,
    TopicViewSet,
    ArticleViewSet,
    CategoryViewSet,
    TopicViewSet,
    ArticleViewSet,
    CategoryViewSet,
    TopicViewSet,
)

router = DefaultRouter()
router.register("category", CategoryViewSet)
router.register("topic", TopicViewSet)
router.register("article", ArticleViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
