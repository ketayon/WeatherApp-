from django.db import models


# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=30, verbose_name="City")
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='City'
        verbose_name_plural='Cities'
        ordering = ['timestamp']