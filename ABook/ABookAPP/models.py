from django.db import models


# Create your models here.
class AddressClass(models.Model):
    slno = models.AutoField(auto_created=True, primary_key=True, verbose_name='ID')
    name = models.CharField(max_length=200)
    phonenumber = models.TextField()
    extension = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()

#< td > {{slno}} < / td > < td > {{name}} < / td > < td > {{phonenumber}} < / td > < td > {{extension}} < / td > < td > {
#    {email}} < / td > < td > {{address}} < / td >