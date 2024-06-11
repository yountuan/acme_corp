from django.db import models

class Product(models.Model):
    category_choices = [
    ("M", "Milk"),
    ("D", "Drinks"),
    ("B", "Bakery"),
    ("MT", "Meat"),
    ("V", "Vegeterian"),
    ("H", "Halal"),

]
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category =  models.CharField(max_length=10, choices=category_choices)
    in_stock = models.BooleanField(default=False)


    def __str__(self) -> str:
        return f'{self.name} - {self.category} - {self.price}'
    
