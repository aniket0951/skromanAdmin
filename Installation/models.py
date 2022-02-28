from django.db import models

# Create your models here.
class SkromanClients(models.Model):
    name =  models.CharField(max_length=60, null=True, blank=True)
    c_type =  models.CharField(max_length=60, null=True, blank=True)
    email =  models.CharField(max_length=60, null=True, blank=True)
    contact =  models.CharField(max_length=60, null=True, blank=True)
    address =  models.CharField(max_length=60, null=True, blank=True)
    city =  models.CharField(max_length=60, null=True, blank=True)
    pin_code =  models.CharField(max_length=60, null=True, blank=True)
    sales_user = models.CharField(max_length=1000, null=True, blank=True)
    ctime = models.DateTimeField(auto_now_add=True)
    uptime = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'clients'  