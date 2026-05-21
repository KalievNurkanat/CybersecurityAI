from rest_framework import serializers
from api.models import RequestData


class RequestDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestData
        fields = ("text", "url", "sender")

