from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthorOrReadOnly(BasePermission):
    """
    Кастомное ограничение. Если запрос от автора - полный доступ.
    Иначе - только безопасные методы.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user


class IsAdminOrReadOnly(BasePermission):
    """
    Кастомное ограничение. Если запрос от админа - полный доступ.
    Иначе - только безопасные методы.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)


class ReadOnly(BasePermission):
    """
    Разрешено только чтение.
    """

    def has_permission(self, request, view):
        return request.method in SAFE_METHODS
