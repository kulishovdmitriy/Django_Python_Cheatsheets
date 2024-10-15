from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

from source.api.serializers_info import (
    InformationSerializer,
    InformationCreateSerializer,
    InformationUpdateDeleteSerializer
)
from source.models import Information


class InfoListAPIView(generics.ListAPIView):
    queryset = Information.objects.all()
    serializer_class = InformationSerializer
    throttle_classes = [AnonRateThrottle, UserRateThrottle]


class InfoCreateAPIView(generics.CreateAPIView):
    queryset = Information.objects.all()
    serializer_class = InformationCreateSerializer
    permission_classes = [IsAdminUser]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]


class InfoUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Information.objects.all()
    serializer_class = InformationUpdateDeleteSerializer
    permission_classes = [IsAdminUser]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
