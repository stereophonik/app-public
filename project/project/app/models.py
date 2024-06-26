from django.db import models

# Create your models here.


class Outcome(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    integer = models.IntegerField()

    class Meta:
        ordering = ['datetime']
