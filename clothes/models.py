from django.db import models


class ClothesType(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class ClothesColor(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class ClothesModel(models.Model):
    class ClothesSize(models.TextChoices):
        XS = "xs", "XS"
        S = "s", "S"
        M = "m", "M"
        L = "l", "L"
        XL = "xl", "Xl"
        XXL = "xxl", "XXL"

    title = models.CharField(max_length=50)
    clothes_type = models.ForeignKey(ClothesType, on_delete=models.PROTECT, related_name="clothes_type")
    price = models.CharField(max_length=10)
    color = models.ForeignKey(ClothesColor, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    size = models.CharField(max_length=5, choices=ClothesSize.choices)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.title
