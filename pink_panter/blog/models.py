from django.db import models




class Manufacture(models.Model):
    full_name = models.CharField(max_length=70)

    def __str__(self):
        return self.full_name


class Product(models.Model):
    pub_date = models.DateField()
    product_name = models.CharField(max_length=200)
    content = models.TextField()
    manufacture = models.ForeignKey(Manufacture, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name
