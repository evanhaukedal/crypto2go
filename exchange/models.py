from django.db import models

# Create your models here.


class Exchange(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField()

    def __str__(self):
        return self.name

    def saveExchange(self):
        self.save()