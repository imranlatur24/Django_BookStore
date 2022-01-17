from django.db import models
from django.utils.timezone import get_current_timezone
class Products(models.Model):
    product_name=models.CharField(max_length=25)
    amount=models.PositiveIntegerField()
    desc=models.TextField(blank=True)
    image=models.ImageField(upload_to="images")
    publisher=models.CharField(max_length=100)
    author=models.CharField(max_length=120,default="")
    date = models.DateTimeField(auto_now_add=True,null=True, blank=True)


    def __str__(self) -> str:
        return self.product_name