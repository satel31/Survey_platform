from rest_framework.permissions import BasePermission


class IsOwnerPermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user

class IsChoiceOwnerPermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user == obj.question.survey.user

class IsSurveyOwnerPermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user == obj.survey.user
