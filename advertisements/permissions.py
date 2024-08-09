from rest_framework.permissions import BasePermission


class AdvertisementPermission(BasePermission):
    def has_permission(self, request, view):
        if view.action == 'list':
            return True
        else:
            return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):

        if view.action in ['update', 'partial_update', 'destroy']:
            return obj.creator == request.user or request.user.is_superuser
        elif view.action == 'mark_as_favorite':
            return obj.creator != request.user
        elif view.action == 'favorite_advertisements':
            return obj.favorite == request.user
        else:
            return False
