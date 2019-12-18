from django.db import models

# Create your models here.

class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Section')
    content = models.TextField(null=True, blank=True, verbose_name='Content')
    image = models.ImageField(upload_to='weatherapp_images/', blank=False)

    class Meta:
        verbose_name_plural = 'Sections'
        verbose_name = 'Section'
        ordering = ['title']

    def __str__(self):
        return self.title