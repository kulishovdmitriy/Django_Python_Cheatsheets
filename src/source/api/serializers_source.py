from rest_framework import serializers

from source.api.serializers_topic import TopicDetailSerializer
from source.models import Source


class SourceSerializer(serializers.ModelSerializer):

    topic = TopicDetailSerializer()

    class Meta:
        model = Source
        fields = ['topic', 'id', 'title', 'description']


class SourceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = '__all__'


class SourceUpdateDeleteSerializer(serializers.ModelSerializer):

    topic = TopicDetailSerializer()

    class Meta:
        model = Source
        fields = '__all__'


class SourceDetailSerializer(serializers.ModelSerializer):

    topic = TopicDetailSerializer()

    class Meta:
        model = Source
        fields = ['topic', 'title']
