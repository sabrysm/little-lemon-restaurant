from django.db import models

class Category(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    slug = models.SlugField()
    title = models.CharField(max_length=255)

class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='menu_items', default=1)
