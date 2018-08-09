from rest_framework import serializers
from contents.models import WantedContent, WantedUrl


class WantedContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = WantedContent
        fields = "__all__"

class WantedUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = WantedUrl
        fields = "__all__"
