from django.db import models
from django.db.models import Model, SlugField
from django.utils.text import slugify


class BaseModel(Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    slug = SlugField(unique=True)

    class Meta:
        abstract = True

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name)
        while self.__class__.objects.filter(slug=self.slug).exists():
            self.slug += '-1'
        super().save(force_insert, force_update, using, update_fields)


class Category(BaseModel):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Product(BaseModel):
    description = models.TextField()
    price = models.FloatField()
    category = models.ForeignKey('apps.Category', on_delete=models.CASCADE, related_name='products')




class ProductImage(Model):
    image = models.ImageField(upload_to='products/')
    product = models.ForeignKey('apps.Product', on_delete=models.CASCADE, related_name='images')

class Cart(Model):
    image = models.ImageField(upload_to='carts/')
    name = models.CharField(max_length=255)
    size = models.FloatField()
    color = models.CharField(max_length=50)
    price = models.FloatField()

    def __str__(self):
        return self.name
