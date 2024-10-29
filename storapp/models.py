from django.contrib.auth import models as auth_models
from django.db import models
from django.urls import reverse

from decimal import Decimal

# Create your models here.
class CodeMemory(models.Model):
    name = models.CharField(max_length=256)
    code = models.CharField(max_length=64)
    owner = models.ForeignKey(auth_models.User, on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add=True)
    unlock_price = models.DecimalField(max_digits=7, decimal_places=2, default=Decimal(0.0))
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        """String for representing code object."""
        return self.name

    def get_absolute_url(self):
        """Returns url to access a particular comment instance."""
        return reverse('code-detail', args=[str(self.id)])

    class Meta:
        ordering = ['upload_date']

class ImageMemory(models.Model):
    name = models.CharField(max_length=256)
    img = models.ImageField()
    owner = models.ForeignKey(auth_models.User, on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add=True)
    unlock_price = models.DecimalField(max_digits=7, decimal_places=2, default=Decimal(0.0))
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        """String for representing code object."""
        return self.name

    def get_absolute_url(self):
        """Returns url to access a particular comment instance."""
        return reverse('image-detail', args=[str(self.id)])

    class Meta:
        ordering = ['upload_date']
