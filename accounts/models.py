from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    name = models.CharField(max_length=30, blank=True, default='')
    self_introduction = models.TextField(blank=True, default='')
    transaction_count = models.IntegerField(default=0)
    review_sum = models.FloatField(default=0)

    class Meta:
        ordering = ('username',)