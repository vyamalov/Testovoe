from rest_framework import serializers
from .models import *


class Source1Serializer(serializers.ModelSerializer):
    image_urls = serializers.StringRelatedField(many=True)
    additional_services = serializers.StringRelatedField(many=True)

    class Meta:
        model = Source1
        fields = '__all__'


class Source2Serializer(serializers.ModelSerializer):
    fuel_price = serializers.StringRelatedField(many=True)

    class Meta:
        model = Source2
        fields = '__all__'

