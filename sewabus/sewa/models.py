from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Sewa(models.Model):
    nama_pemesan = models.CharField(max_length=240, null=True,blank=False)
    no_ktp = models.CharField(blank=False,null=True,  max_length=50)
    # alamat = models.CharField(max_length=100, null=True,blank=False)
    no_hp = models.CharField(blank=False,null=True, max_length=50)
    email = models.EmailField(blank=False, max_length=254)
    tanggal_mulai =  models.DateField(blank=False, auto_now=False, auto_now_add=False, null=True)
    tanggal_selesai =  models.DateField(blank=False, auto_now=False, auto_now_add=False, null=True)
    titik_penjemputan =models.TextField(blank=False, max_length=254)

def __str__(self):
    return self.nama_pemesan



