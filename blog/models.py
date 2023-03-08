from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.


class TypeCategory(models.Model):
    category = models.CharField(max_length=60, unique=True, null=False,
                                blank=False)

    def __str__(self):
        return self.category


class Spice(models.Model):
    use_category = [
                    ('medicinal', 'medicinal'),
                    ('baking', 'baking'),
                    ('cooking', 'cooking'), ]
    slug = models.SlugField(max_length=60, null=False, unique=True)
    name = models.CharField(max_length=60, null=False, blank=False)
    image = CloudinaryField(default='placeholder', max_length=255,
                            verbose_name='image')
    date_created = models.DateField(auto_now_add=True,
                                    null=False, blank=False)
    description = models.TextField(max_length=1000, null=False, blank=False)
    use_category = models.CharField(max_length=20,
                                    choices=use_category,
                                    null=False, blank=False)
    type_category = models.ManyToManyField(TypeCategory, related_name='type',
                                           blank='True')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    bookmark = models.ManyToManyField(User, related_name='bookmark',
                                      blank='True')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='comment')
    spice = models.ForeignKey(Spice, on_delete=models.CASCADE,
                              related_name='comment')
    body = models.TextField(max_length=100)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

