from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    """Класс постов."""

    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True)
    group = models.ForeignKey(
        'Group', on_delete=models.SET_NULL,
        related_name='posts', blank=True, null=True
    )

    def __str__(self):
        return self.text


class Comment(models.Model):
    """Класс комментариев."""

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)


class Group(models.Model):
    """Класс групп."""

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class Follow(models.Model):
    """Класс подписок."""

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user')
    following = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='following'
    )

    class Meta:
        """Meta."""

        constraints = [
            models.UniqueConstraint(
                fields=['user', 'following'], name='unique_user_following'
            )
        ]
