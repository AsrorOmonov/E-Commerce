from django.db import models


# Create your models here.
class TypeModel(models.Model):
    title = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'type'
        verbose_name_plural = 'types'


class BrandModel(models.Model):
    name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'brand'
        verbose_name_plural = 'brands'


class OutfitModel(models.Model):
    title = models.CharField(max_length=20)
    type = models.ForeignKey(TypeModel, on_delete=models.PROTECT, related_name='outfit')
    brand = models.ForeignKey(BrandModel, on_delete=models.PROTECT, related_name='outfit')
    cover = models.ImageField(upload_to='cover')
    price = models.CharField(max_length=10, null=True)
    summary = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'outfit'
        verbose_name_plural = 'outfits'
