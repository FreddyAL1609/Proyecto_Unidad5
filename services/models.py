from django.db import models

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    logo = models.URLField(max_length=200)

    def __str__(self):
        return self.name
