from rest_framework import generics

from source.api.serializers_source import SourceSerializer, SourceCreateSerializer, SourceUpdateDeleteSerializer
from source.models import Source


class SourceListAPIView(generics.ListAPIView):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer


class SourceCreateAPIView(generics.CreateAPIView):
    queryset = Source.objects.all()
    serializer_class = SourceCreateSerializer


class SourceUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Source.objects.all()
    serializer_class = SourceUpdateDeleteSerializer
