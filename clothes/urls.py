from django.urls import path
from clothes.views import ClothesAPIView, ClothesDetailAPIView, ClothesCreateAPIView

app_name = "clothes"

urlpatterns = [
    path("clothes/detail/<int:pk>/", ClothesDetailAPIView.as_view(), name="clothes_detail"),
    path("clothes/", ClothesAPIView.as_view(), name="clothes"),
    path("clothes/create", ClothesCreateAPIView.as_view(), name="clothes_create")

]
