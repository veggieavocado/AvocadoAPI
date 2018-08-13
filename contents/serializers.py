from rest_framework import serializers
from contents.models import WantedContent, WantedUrl, WantedData


class WantedContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = WantedContent
        fields = "__all__"

class WantedUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = WantedUrl
        fields = "__all__"

class WantedDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = WantedData
        fields = "__all__"
