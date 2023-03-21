from django.db import models

# Create your models here.


class FilteredImage(models.Model):
    image = models.ImageField(upload_to='filtered_images')
