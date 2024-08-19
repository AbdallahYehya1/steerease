from django.db import models
from django.contrib.sessions.models import Session
class Product(models.Model):
    name = models.CharField(max_length=255)  # Name of the product
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price with two decimal places
    material = models.CharField(max_length=100)  # Material the product is made of
    gender = models.CharField(max_length=50, choices=[('M', 'Male'), ('F', 'Female')])  # Gender category

    def __str__(self):
        return self.name
class Size(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Foreign key to the Product table
    size_name = models.CharField(max_length=50)  # Name of the size (e.g., Small, Medium, Large)
    size_quantity = models.PositiveIntegerField()  # Quantity of this size for the product

    class Meta:
        unique_together = ('product', 'size_name')  # Composite unique constraint

    def __str__(self):
        return f'{self.size_name} - {self.product.name}'
    
class images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Foreign key to the Product table
    url = models.CharField(max_length=255)  # Name of the size (e.g., Small, Medium, Large)
    

    class Meta:
        unique_together = ('product', 'url')  # Composite unique constraint

    def __str__(self):
        return f'{self.url} - {self.product.name}'    
    
class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Foreign key to Product
    session = models.ForeignKey(Session, on_delete=models.CASCADE)  # Foreign key to Session
    size = models.ForeignKey(Size, on_delete=models.CASCADE)  # Foreign key to Size
    imageUrl = models.URLField(default='http://example.com/default.jpg') 
    quantity = models.PositiveIntegerField(default=1)  # Quantity of the product in the cart

    class Meta:
        unique_together = ('product', 'session', 'size')  # Ensure each product+size combination is unique in a session

    def __str__(self):
        return f'{self.product.name} ({self.size.size_name}) - {self.quantity} items in Cart'    