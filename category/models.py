# from audioop import reverse
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.
class Category(models.Model):
     category_name = models.CharField(max_length=50,unique=True)
     slug = models.SlugField(max_length=100,unique=True)
     description =models.TextField(max_length=300,blank=True)
     cat_image = models.ImageField(upload_to = 'photo/categories',blank = True)

     class Meta:
          verbose_name = "Category"
          verbose_name_plural = "Categories"
          
     def get_url(self):
          return reverse('products_by_category',args=[self.slug])

     def __str__(self):
          return self.category_name
     
     # def get_absolute_url(self):
     #      return reverse("category_detail", kwargs={"pk": self.pk})
     def save(self, *args, **kwargs):  # new
        if self.slug:
            self.slug = slugify(self.category_name)
        return super().save(*args, **kwargs)
