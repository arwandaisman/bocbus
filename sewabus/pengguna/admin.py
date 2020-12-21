from django.contrib import admin

from pengguna.models import DataBus, Images




class AdminBus(admin.ModelAdmin):
    list_display = ['judul','merk_seri_bus', 'no_plat', 'kategori','jml_kursi']
    search_fields = ['judul','merk_seri_bus']
    # list_filter = ('jml_kursi')
    # list_per_page = 4

class AdminImage(admin.ModelAdmin):
    list_display = ['post','image']

admin.site.register(DataBus, AdminBus)
admin.site.register(Images, AdminImage)
