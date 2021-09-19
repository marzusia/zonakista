from django.db import models

class City(models.Model):
    name = models.CharField(max_length=128)
    population = models.IntegerField(null=True, blank=True)
    etymology = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Cities'