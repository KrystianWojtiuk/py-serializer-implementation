from rest_framework import serializers


class CarSerializer(serializers.Serializer):
    manufacturer = serializers.CharField(max_length=64, required=True)
    model = serializers.CharField(max_length=64, required=True)
    horse_powers = serializers.IntegerField(
        min_value=1,
        max_value=1914,
        required=True
    )
    is_broken = serializers.BooleanField(required=True)
    problem_description = serializers.CharField(
        required=False,
        allow_blank=True)
