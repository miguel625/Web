from django.db import models

# Create your models here.
class Login (models.Model):
    nombre = models.CharField(max_length = 254,null=False)
    ap_pat = models.CharField(max_length = 254,null=False)
    ap_mat = models.CharField(max_length = 254,null=False)
    edad = models.IntegerField(null=False)