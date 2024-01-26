from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True

class Category(BaseModel):
    slug = models.SlugField(unique=True, blank=True)
    name = models.CharField(max_length=100)

    def product_count(self):
        return self.product_set.count()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        if self.slug and self.name:
            self.slug = slugify(self.name)        
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'


class Brand(BaseModel):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=100)
    
    def product_count(self):
        return self.product_set.count()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        if self.slug and self.name:
            self.slug = slugify(self.name)  
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'brand'


class Product(BaseModel):
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def first_image(self):
        first_image = self.image_set.first()  # İlk görseli al
        if first_image:
            return first_image.image.url  # Görsel URL'sini döndür
        return None

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.brand} {self.name}"

    class Meta:
        db_table = 'product'


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField()

    class Meta:
        db_table = 'image'
