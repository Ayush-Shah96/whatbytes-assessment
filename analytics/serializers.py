from rest_framework import serializers


class AnalyticsSerializer(serializers.Serializer):
    """Serializer for analytics data."""
    metric_name = serializers.CharField()
    value = serializers.IntegerField()
    timestamp = serializers.DateTimeField()
