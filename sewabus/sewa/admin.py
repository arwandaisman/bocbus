from django.contrib import admin

from sewa.models import Sewa




class AdminSewa(admin.ModelAdmin):
    list_display = ['nama_pemesan','no_hp', 'email', 'tanggal_mulai','tanggal_selesai', 'titik_penjemputan']
    search_fields = ['nama_pemesan']
    
admin.site.register(Sewa, AdminSewa)


