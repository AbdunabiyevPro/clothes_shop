from rest_framework import serializers
from .models import ClothesModel


class ClothesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClothesModel
        fields = ['id', 'title', 'clothes_type', 'price', 'color', 'description', 'size', 'stock']
