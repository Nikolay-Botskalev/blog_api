from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import filters, mixins, status, viewsets
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .permissions import IsAuthorOrReadOnly
from posts.models import Follow, Group, Post
from .serializers import (
    CommentSerializer, FollowSerializer, GroupSerializer, PostSerializer)

User = get_user_model()


class PostViewSet(viewsets.ModelViewSet):
    """Класс-обработчик запросов к модели Post."""

    queryset = Post.objects.select_related('author')
    permission_classes = (IsAuthorOrReadOnly,)
    pagination_class = LimitOffsetPagination
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(author=self.request.user)
        else:
            raise AuthenticationFailed("Не авторизован.")


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Класс-обработчик запросов к модели Group."""

    serializer_class = GroupSerializer
    queryset = Group.objects.all()


class CommentViewSet(viewsets.ModelViewSet):
    """Класс-обработчик запросов к модели Comment."""

    serializer_class = CommentSerializer
    pk_url_kwarg = 'comment_id'
    permission_classes = (IsAuthorOrReadOnly,)

    def get_post(self):
        post_id = self.kwargs['post_id']
        return get_object_or_404(Post, id=post_id)

    def get_queryset(self):
        post = self.get_post()
        return post.comments.select_related('author').filter(post=post.id)

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(post=self.get_post(), author=self.request.user)
        else:
            raise AuthenticationFailed("Не авторизован.")


class FollowViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):

    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter, )
    search_fields = ('following__username',)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Follow.objects.select_related('user').filter(
            user=self.request.user
        )

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED)
