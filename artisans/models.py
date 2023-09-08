from django.db import models

# Create your models here.


class Artisan(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    contact_email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    profile_image = models.ImageField(
        upload_to='artisan_profiles/', blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    artisan = models.ForeignKey(Artisan, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to='product_images/')
    category = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class CustomOrder(models.Model):
    customer_name = models.CharField(max_length=100)
    artisan = models.ForeignKey(Artisan, on_delete=models.CASCADE)
    description = models.TextField()
    order_date = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Custom Order for {self.artisan} by {self.customer_name}"


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    rating = models.PositiveIntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.customer_name} for {self.product}"
