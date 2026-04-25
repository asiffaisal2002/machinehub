from django.db import models

class register(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.email


class addproduct(models.Model):
    product_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.product_name


class rent(models.Model):
    product = models.ForeignKey(addproduct, on_delete=models.CASCADE)
    user = models.ForeignKey(register, on_delete=models.CASCADE)
    rent_date = models.DateField(auto_now_add=True)
    return_date = models.DateField()

