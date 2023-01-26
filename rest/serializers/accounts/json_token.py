from rest_framework import serializers


class JSONTokenSerializer(serializers.Serializer):
    """
    Auth token serializer
    """
    token = serializers.CharField()
