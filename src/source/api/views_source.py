from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

from source.api.serializers_source import SourceSerializer, SourceCreateSerializer, SourceUpdateDeleteSerializer
from source.models import Source


class SourceListAPIView(generics.ListAPIView):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer
    throttle_classes = [AnonRateThrottle, UserRateThrottle]


class SourceCreateAPIView(generics.CreateAPIView):
    queryset = Source.objects.all()
    serializer_class = SourceCreateSerializer
    permission_classes = [IsAdminUser]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]


class SourceUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Source.objects.all()
    serializer_class = SourceUpdateDeleteSerializer
    permission_classes = [IsAdminUser]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
