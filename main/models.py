from django.db import models

# Create your models here.
class Product(models.Model):
    CATEGORY_CHOICES = [('shoe', 'Shoe'), ('jersey', 'Jersey'), ('accessory', 'Accessory'), ('shorts', 'Shorts')]
    
    name = models.CharField()
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='jersey')
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name