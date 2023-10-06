from rest_framework import serializers

from apps.survey.models import View


class ViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = View
        fields = '__all__'
