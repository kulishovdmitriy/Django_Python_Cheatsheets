from rest_framework import serializers

from source.models import Topic


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['id', 'name']


class TopicCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'


class TopicUpdateDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'


class TopicDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['name']
