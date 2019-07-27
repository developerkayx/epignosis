from rest_framework import serializers

from .models import *


# Define your Serializers here
class MessageSerializer(serializers.ModelSerializer):
    album_name = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Message
        fields = '__all__'


class PartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields = '__all__'


class CollectionSerializer(serializers.ModelSerializer):
    parts = PartSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Collection
        fields = '__all__'