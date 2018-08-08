from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=200, blank=False)
    email = models.EmailField(max_length=128, blank=False)

    def __str__(self):
        return self.name