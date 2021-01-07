from django.contrib import admin

from pengguna.models import DataBus, Images, Ketersediaan




class AdminBus(admin.ModelAdmin):
    list_display = ['judul','merk_seri_bus', 'kategori','jml_kursi']
    search_fields = ['judul','merk_seri_bus']
    # list_filter = ('jml_kursi')
    # list_per_page = 4

class AdminImage(admin.ModelAdmin):
    list_display = ['post','image']

class AdminKetersediaan(admin.ModelAdmin):
    list_display = ['sedia','tanggal_mulai', 'tanggal_selesai', 'nama_penyewa', 'no_hp_penyewa', 'nik']

admin.site.register(DataBus, AdminBus)
admin.site.register(Images, AdminImage)
admin.site.register(Ketersediaan, AdminKetersediaan)
