from django.db import models

class DeleviryInformation(models.Model):

    name = models.CharField(max_length=100)

    age = models.PositiveIntegerField()

    city = models.CharField(max_length=100)
    
    gender = models.CharField(max_length=20)

    description = models.TextField(blank=True)

    def __str__(self):
        return self.name