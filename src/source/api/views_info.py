from rest_framework import generics

from source.api.serializers_info import (
    InformationSerializer,
    InformationCreateSerializer,
    InformationUpdateDeleteSerializer
)
from source.models import Information


class InfoListAPIView(generics.ListAPIView):
    queryset = Information.objects.all()
    serializer_class = InformationSerializer


class InfoCreateAPIView(generics.CreateAPIView):
    queryset = Information.objects.all()
    serializer_class = InformationCreateSerializer


class InfoUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Information.objects.all()
    serializer_class = InformationUpdateDeleteSerializer
