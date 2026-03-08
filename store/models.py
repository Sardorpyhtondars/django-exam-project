from django.db import models

from shared.models import BaseModel


class Stores(BaseModel):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='store/')
    price = models.CharField(max_length=100)
    reviews = models.CharField(max_length=100)
