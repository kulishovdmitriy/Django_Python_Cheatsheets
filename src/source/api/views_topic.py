from rest_framework import generics

from source.models import Topic
from source.api.serializers_topic import TopicSerializer, TopicUpdateDeleteSerializer, TopicCreateSerializer


class TopicListAPIView(generics.ListAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class TopicCreateAPIView(generics.CreateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicCreateSerializer


class TopicUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicUpdateDeleteSerializer
