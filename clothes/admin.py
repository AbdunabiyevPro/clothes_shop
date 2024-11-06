from django.contrib import admin
from clothes.models import ClothesModel, ClothesColor, ClothesType


@admin.register(ClothesModel)
class ClothesModelAdmin(admin.ModelAdmin):
    list_display = ['title', "price"]




@admin.register(ClothesType)
class ClothesTypeAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(ClothesColor)
class ClothesColorModel(admin.ModelAdmin):
    list_display = ['title']