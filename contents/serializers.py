from rest_framework import serializers
from contents.models import WantedContent


class WantedContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = WantedContent
        fields = "__all__"
