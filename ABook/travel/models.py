from django.db import models

# Create your models here.

class Destination:
    # id: int
    # name: str
    # img: str
    # address: str
    # desc: str
    # price: int
    # offer: bool
    #slno = models.AutoField(auto_created=True, primary_key=True, verbose_name='ID')
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='images')
    address = models.TextField()
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
