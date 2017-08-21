from django.db import models
from django.conf import settings

# Create your models here.
class Errand(models.Model):
    CATEGORY_CHOICES = (
        ("DELIVERY","Delivery"),
        ("HOMEWORK","Homework"),
        ("ETC","Etc"),
    )
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='errands', null=True, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='Blank Title')
    text = models.TextField()
    extraCost = models.PositiveIntegerField()
    reward = models.PositiveIntegerField()
    category = models.CharField(max_length=10, 
            choices=CATEGORY_CHOICES, 
            default="DELIVERY" )
    class Meta:
        ordering = ('-created',)


class Candidate(models.Model):
    errand = models.ForeignKey(Errand, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)