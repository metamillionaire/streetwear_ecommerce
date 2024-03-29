from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product

# Create your models here. Get the user model
User = get_user_model()


# Cart Model
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    purchased = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.quantity} of {self.item.name}'

    # Getting the total price

    def get_total(self):
        return self.item.price * self.quantity

# Order Model 
class Order(models.Model):
    orderitems = models.ManyToManyField(Cart)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    
    def get_totals(self):
        total = 0
        for order_item in self.orderitems.all():
            total += order_item.get_total()

        return total


