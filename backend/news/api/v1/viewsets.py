from rest_framework import authentication
from news.models import (
    Category,
    Topic,
    Article,
    Article,
    Category,
    Topic,
    Article,
    Category,
    Topic,
)
from .serializers import (
    CategorySerializer,
    TopicSerializer,
    ArticleSerializer,
    ArticleSerializer,
    CategorySerializer,
    TopicSerializer,
    ArticleSerializer,
    CategorySerializer,
    TopicSerializer,
)
from rest_framework import viewsets


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Category.objects.all()


class TopicViewSet(viewsets.ModelViewSet):
    serializer_class = TopicSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Topic.objects.all()


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Article.objects.all()
