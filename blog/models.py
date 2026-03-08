from django.db import models

from shared.models import BaseModel


class Blogs(BaseModel):
    date = models.DateField()
    title = models.CharField(max_length=100)
    comments = models.CharField(max_length=100)

