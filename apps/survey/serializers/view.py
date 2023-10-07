from rest_framework import serializers

from apps.survey.models import View


class ViewSerializer(serializers.ModelSerializer):
    """Сериализатор для просмотра опроса"""

    class Meta:
        model = View
        fields = '__all__'
