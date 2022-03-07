from django.db import models


# Create your models here.
class movie(models.Model):
    name = models.CharField(max_length=30)
    des = models.TextField()
    year = models.IntegerField()
    im = models.ImageField(upload_to='imag')

    def __str__(self):
        return self.name
