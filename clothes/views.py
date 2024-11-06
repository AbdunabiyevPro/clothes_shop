from rest_framework import generics
from clothes.serializers import ClothesSerializer
from clothes.models import ClothesModel
from rest_framework.response import Response
from rest_framework import status


class ClothesDetailAPIView(generics.RetrieveAPIView):
    serializer_class = ClothesSerializer
    queryset = ClothesModel.objects.all()


class ClothesAPIView(generics.ListAPIView):
    serializer_class = ClothesSerializer
    queryset = ClothesModel.objects.all()


class ClothesCreateAPIView(generics.CreateAPIView):
    serializer_class = ClothesSerializer
    queryset = ClothesModel.objects.all()
