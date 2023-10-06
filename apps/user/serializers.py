from rest_framework import serializers

from django.contrib.auth.hashers import make_password

from apps.survey.serializers.like import LikeSerializer
from apps.survey.serializers.survey import SurveySerializer
from apps.survey.serializers.view import ViewSerializer
from apps.user.models import User


class UserSerializer(serializers.ModelSerializer):
    assessments = LikeSerializer(many=True, read_only=True)
    surveys = SurveySerializer(many=True, read_only=True)
    views = ViewSerializer(many=True, read_only=True)

    def validate_password(self, value: str) -> str:
        return make_password(value)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'city', 'avatar', 'phone', 'password')


class StrangerUserSerializer(serializers.ModelSerializer):
    assessments = LikeSerializer(many=True, read_only=True)
    surveys = SurveySerializer(many=True, read_only=True)
    views = ViewSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('first_name', 'email', 'city', 'avatar', 'phone', 'telegram',)
