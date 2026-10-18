from django.db import models


class CosmicObject(models.Model):
    name = models.CharField(max_length=100)
    object_type = models.CharField(max_length=100)
    fact = models.TextField()

    diameter = models.CharField(max_length=100, blank=True)
    distance_from_sun = models.CharField(max_length=100, blank=True)
    moons = models.CharField(max_length=100, blank=True)
    year_length = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name