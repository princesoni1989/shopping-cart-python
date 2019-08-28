from .customers import *


class ProductCategory(models.Model):
    category = models.CharField(max_length=50)
    description = models.TextField(max_length=100)
    background_image = models.ImageField(upload_to='product/', default='product/default.png')
    seo_title = models.CharField(max_length=20)
    seo_description = models.TextField(max_length=100)

    class Meta:
        verbose_name_plural = "Product Category"

    def __str__(self):
        return self.category


class Products(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=False)
    description = models.TextField(max_length=100)
    price = models.FloatField()
    publication_date = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    quantity = models.PositiveIntegerField(default=1)
    is_published = models.BooleanField(default=False)
    seo_title = models.CharField(max_length=20)
    seo_description = models.TextField(max_length=100)
    tax = models.FloatField()
    weight = models.FloatField()

    class Meta:
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name


class ProductImages(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product/', default='product/default.png')

    class Meta:
        verbose_name_plural = "Product Images"


class ProductColors(models.Model):
    product = models.ManyToManyField(Products)
    color = models.TextField(max_length=20)

    class Meta:
        verbose_name_plural = "Product Color"

    def __str__(self):
        return self.color
