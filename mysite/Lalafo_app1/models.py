from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Category(models.Model):
    category_name = models.CharField(max_length=30, unique=True)
    category_image = models.ImageField(
        upload_to='cat_images',
        null=True,
        blank=True
    )

    def __str__(self):
        return  self.category_name

class Product(models.Model):
    product_name = models.CharField(max_length=60)
    price = models.PositiveIntegerField()
    phone_number = PhoneNumberField()
    product_image = models.ImageField(
        upload_to='product_images',
        null=True,
        blank=True
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    product_type = models.BooleanField(default=False)
    description = models.TextField()
    city = models.CharField(max_length=30 )
    created = models.DateField(auto_now_add=True)
    original = models.BooleanField(default=False)

    def __str__(self):
        return  self.product_name