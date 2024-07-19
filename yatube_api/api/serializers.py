from django.contrib.auth import get_user_model

from rest_framework import serializers

from posts.models import Comment, Follow, Group, Post

User = get_user_model()


class AuthorMixinForSerializer(serializers.ModelSerializer):
    """Миксин для переопределения поля автора."""

    author = serializers.SlugRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault(),
        slug_field='username')


class PostSerializer(AuthorMixinForSerializer):
    """Сериализатор модели постов."""

    class Meta:
        """Meta."""

        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        read_only_fields = ('id', 'author', 'post', 'created')
        model = Comment


class GroupSerializer(serializers.ModelSerializer):
    """Сериализатор модели групп."""

    class Meta:
        """Meta."""

        fields = '__all__'
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    """Сериализатор для подписок."""

    user = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all(),
        required=True
    )

    class Meta:
        """Meta."""

        fields = ('user', 'following',)
        model = Follow
