from rest_framework import serializers


class DetailResponseSerializer(serializers.Serializer):
    detail = serializers.CharField(read_only=True)


class NonFieldErrorResponseSerializer(serializers.Serializer):
    non_field_errors = serializers.CharField(read_only=True)
