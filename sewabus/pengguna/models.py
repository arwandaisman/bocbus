from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Hotel(models.Model): 
    name = models.CharField(max_length=50) 
    hotel_Main_Img = models.ImageField(upload_to='images/') 

# class Jenis(models.Model):
#     jenis = models.CharField(max_length = 10)

#     def __str__(self):
#         return self.jenis 


class DataBus(models.Model):
    jenis_bus = (
        ('kecil', 'Kecil'),
        ('medium', 'Medium'),
        ('besar', 'Besar'),
    )

    merk_seri_bus = (
        ('Scania', 'Scania'),
        ('Hino', 'Hino'),
        ('Mercedez Benz', 'Mercedez Benz'),
        ('Volvo', 'Volvo'),
        ('Mitsubishi Fuso', 'Mitsubishi Fuso'),
        ('Toyota Dyana', 'Toyota Dyana'),
        ('Zhong Thong', 'Zhong Thong'),
    )

    judul = models.CharField(max_length = 100,default=None)
    merk_seri_bus =  models.CharField(max_length = 100,choices=merk_seri_bus,default=None, null=True)
    tahun_pembuatan =  models.IntegerField(default=2015)
    no_plat = models.CharField(max_length = 15,default=None)
    kategori = models.CharField(max_length=10, choices=jenis_bus,default=None, null=True)
    harga_12jam = models.IntegerField(default=500000)
    harga_fullday = models.IntegerField(default=1000000)
    jml_kursi = models.IntegerField(default=None)
    jml_bus= models.IntegerField(default=None)
    ac = models.CharField(max_length = 15,default=None, blank=True, null=True)
    dvd = models.CharField(max_length = 15,default=None, blank=True, null=True)
    toilet = models.CharField(max_length = 15,default=None, blank=True, null=True)
    stop_kontak = models.CharField(max_length = 15,default=None, blank=True, null=True)
    sabuk_pengaman = models.CharField(max_length = 15,default=None, blank=True, null=True)
    bagasi = models.CharField(max_length = 15,default=None, blank=True, null=True)
    wifi = models.CharField(max_length = 15,default=None, blank=True, null=True)
    tv = models.CharField(max_length = 15,default=None, blank=True, null=True)
    bantal = models.CharField(max_length = 15,default=None, blank=True, null=True)
    selimut = models.CharField(max_length = 15,default=None, blank=True, null=True)
    smoking_area = models.CharField(max_length = 15,default=None, blank=True, null=True)
    # ac = models.BooleanField("ac", default=False)
    # dvd = models.BooleanField("DVD/Video", default=False)
    # toilet = models.BooleanField("Toilet", default=False)
    # stop_kontak = models.BooleanField("Stop Kontak", default=False)
    # sabuk_pengaman = models.BooleanField("Sabuk Pengaman", default=False)
    # bagasi = models.BooleanField("Bagasi", default=False)
    # wifi = models.BooleanField("WIFI", default=False)
    # tv = models.BooleanField("TV", default=False)
    # bantal = models.BooleanField("Bantal", default=False)
    # selimut = models.BooleanField("Selimut", default=False)
    # smoking_area = models.BooleanField("Smoking Area", default=False)
    # img = models.ImageField(upload_to='gambar/',blank=True)
    tambahan = models.TextField(default=None,null=True)
    po_id = models.ForeignKey(User, on_delete = models.DO_NOTHING,related_name='po_id',)
    

    def __str__(self): 
        return self.judul 
      
class Images(models.Model):
    post = models.ForeignKey(DataBus, default=None, on_delete=models.CASCADE, related_name= 'images')
    image = models.ImageField(upload_to = 'gambar/', blank=True, null = True)
    def __str__(self):
        return self.post.no_plat + " Image"



# class Provinsi(models.Model):
#     nama = models.CharField(max_length=30)

#     def __str__(self):
#         return self.nama

class Kabupaten(models.Model):
    # provinsi = models.ForeignKey(Provinsi, on_delete=models.CASCADE)
    nama = models.CharField(max_length=30)

    def __str__(self):
        return self.nama
    
class Biaya(models.Model):
    kabupaten = (
        ('Sleman', 'Sleman'), ('Kulon_Progo', 'KulonProgo')
    )

    nama = models.ForeignKey(DataBus, default=None, on_delete=models.CASCADE, related_name= 'biaya')
    # provinsi_asal =  models.ForeignKey(Provinsi, on_delete=models.SET_NULL, null=True)
    kabupaten_asal = models.CharField(max_length = 100,choices=kabupaten,default=None, null=True)
    # provinsi_tujuan = models.ForeignKey(Provinsi, on_delete=models.SET_NULL, null=True)
    kabupaten_tujuan = models.CharField(max_length = 100,choices=kabupaten,default=None, null=True)
    harga = models.IntegerField(default=500000)
    def __str__(self): 
        return self.nama



class Profil(models.Model):
    nama_perusahaan = models.CharField(max_length = 100,default=None)
    foto_profil = models.ImageField(upload_to='gambar/',blank=True)
    tanggal_berdiri =  models.DateField()
    no_tlpn = models.CharField(max_length = 15,default=False, blank=True  )
    no_hp = models.CharField(max_length = 15,default=+62 )
    email = models.EmailField(max_length=254, default=None, null=True)
    provinsi = models.CharField(max_length=50, default=False)
    kabupaten_kota= models.CharField(max_length = 15,default=False)
    kecamatan = models.CharField(max_length=50, default=False)
    kode_pos = models.IntegerField(default=False)
    alamat_lengkap = models.TextField(default=None,null=True)
    bio= models.TextField(default=None,blank=True)
    
    def __str__(self):
        return self.nama_perusahaan