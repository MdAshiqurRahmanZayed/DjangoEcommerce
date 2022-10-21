from django.urls import reverse
from django.db import models
from category.models import Category
from django.utils.text import slugify
# Create your models here.
class Product(models.Model):
     product_name = models.CharField(max_length = 200,unique = True)
     slug         = models.SlugField(max_length = 200,unique = True)
     description  = models.TextField(max_length = 500,blank=True)
     price        = models.IntegerField()
     images       = models.ImageField( upload_to='photo/products')
     stock        = models.IntegerField()
     is_available = models.BooleanField()
     category     = models.ForeignKey(Category, on_delete=models.CASCADE)
     created_at   = models.DateTimeField( auto_now_add=True)
     modified_at  = models.DateTimeField( auto_now=True)
     
     
     def get_url(self):
        return reverse('product_detail',args=[self.category.slug,self.slug])
     
     def __str__(self):
         return self.product_name     
      
      
      
     def save(self, *args, **kwargs):  # new
        if self.slug:
            self.slug = slugify(self.product_name)
        return super().save(*args, **kwargs)