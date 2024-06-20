from rest_framework import serializers
from .models import Movie

def name_length(value):
    """
    validators validation level
    """
    if len(value) < 5:
        raise serializers.ValidationError("Name is too short!")


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(validators=[name_length])
    description = serializers.CharField()
    active = serializers.BooleanField()

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.description = validated_data.get("description", instance.description)
        instance.save()
        return instance
       
    def validate_name(self, value):
        """
        Field validation level
        """
        if len(value) < 5:
            raise serializers.ValidationError("Name is too short!")
        return value
        
    def validate(self, data):
        """
        Object validation level
        """
        if data['name'] == data['description']:
            raise serializers.ValidationError("Title and description should be different!")
        return data