from django.db import models
from django.contrib.auth.models import User
from django.utils.html import mark_safe
from django.core.exceptions import ValidationError
from easy_thumbnails.fields import ThumbnailerImageField


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()

    def __str__(self):
        return self.user.username


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    user = models.ForeignKey(
        Author,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    name = models.CharField(max_length=200, null=True, blank=True)
    image = ThumbnailerImageField(
        upload_to='products/%Y/m%d/',
        blank=True,
        null=True
    )
    brand = models.CharField(max_length=200, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    rating = models.DecimalField(max_digits=7, decimal_places=2)
    numReviews = models.PositiveIntegerField(default=0, null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    countInStock = models.IntegerField(null=True, blank=True, default=0)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def image_tag(self):
        return mark_safe(
            '<img src="%s" width="100px" height="80px" />' % (self.image.url)
        )
    image_tag.short_description = 'Image'

    def clean(self):
        if len(self.name) < 5:
            raise ValidationError(
                {
                    'name': 'Title shoud have at least 5 letters.'
                }
            )
