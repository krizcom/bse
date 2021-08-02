from django.db import models

class employee(models.Model):
    idlogin =  models.IntegerField()
    empid = models.IntegerField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    authrank = models.CharField(max_length=1)

