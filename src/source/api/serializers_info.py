from rest_framework import serializers

from source.api.serializers_source import SourceDetailSerializer
from source.models import Information


class InformationSerializer(serializers.ModelSerializer):

    source = SourceDetailSerializer()

    class Meta:
        model = Information
        fields = ['id', 'text', 'source']


class InformationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = '__all__'


class InformationUpdateDeleteSerializer(serializers.ModelSerializer):

    source = SourceDetailSerializer()

    class Meta:
        model = Information
        fields = '__all__'
