from rest_framework import serializers
from .models import Part

class PartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields = '__all__'

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("The 'name' field cannot be empty.")
        return value

    def validate_sku(self, value):
        if not value.strip():
            raise serializers.ValidationError("The 'sku' field cannot be empty.")
        return value

    def validate_description(self, value):
        if not value.strip():
            raise serializers.ValidationError("The 'description' field cannot be empty.")
        return value

    def validate_weight_ounces(self, value):
        if value <= 0:
            raise serializers.ValidationError("The 'weight_ounces' must be greater than 0.")
        return value

    def validate(self, data):
        required_fields = ['name', 'sku', 'description', 'weight_ounces', 'is_active']
        missing_fields = [field for field in required_fields if field not in data]

        if missing_fields:
            raise serializers.ValidationError(
                f"Missing required fields: {', '.join(missing_fields)}"
            )

        return data
