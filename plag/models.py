from django.db import models

# Create your models here.
class Query(models.Model):
    percentage = models.CharField(max_length=3)
    path = models.CharField(max_length=100)
    file = models.CharField(max_length=2000)

    def __str__(self):
        return self.file[:5] 