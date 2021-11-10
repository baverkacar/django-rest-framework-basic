from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission): 
    """ Allow user to edit their own profile """

    def has_object_permission(self, request, view, obj):
        """ Check user is trying to edit their own profile """

        if request.method in permissions.SAFE_METHODS: # GET 
            return True

        return obj.id == request.user.id
        return super().has_object_permission(request, view, obj)

