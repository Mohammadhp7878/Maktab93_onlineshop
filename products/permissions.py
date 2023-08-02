from rest_framework import permissions


class IsCommentOwner(permissions.BasePermission):
    '''
    customize permission class in order to allows only the comment owner to update or delete comments.
    '''
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user