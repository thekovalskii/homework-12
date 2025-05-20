from django.db import models

# Create your models here.


rate_choices = (
    ('1', 1),
    ('2', 2),
    ('3', 3),
    ('4', 4),
    ('5', 5),
)


class Product(models.Model):
    title = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    rate = models.IntegerField(choices=rate_choices, default=5)
