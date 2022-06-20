from rest_framework import viewsets
from webapp.models import ZhebsaWord, PhelkayWord
from .serializer import AllWordSerializer, ZhebsaPhelkaySerializer, ZhebsaWordSerializer, PhelkayWordSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class ZhebsaWordViewSet(viewsets.ModelViewSet):
    serializer_class = ZhebsaWordSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return ZhebsaWord.objects.all()

class PhelkayWordViewSet(viewsets.ModelViewSet):
    serializer_class = PhelkayWordSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return PhelkayWord.objects.all()

class ZhebsaPhelkayViewSet(viewsets.ModelViewSet):
    serializer_class = ZhebsaPhelkaySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return ZhebsaWord.objects.all()

class AllWordViewSet(viewsets.ModelViewSet):
    serializer_class = AllWordSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return ZhebsaWord.objects.all()