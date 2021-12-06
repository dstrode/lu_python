from django.db import models

class User(models.Model):

    lietotajs = models.CharField(max_length=100)
    epasts = models.EmailField(max_length=110)
    image = models.ImageField(upload_to='lietotaji', blank=True)








