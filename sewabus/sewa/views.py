from django.shortcuts import render, redirect
from . import models
from pengguna.models import DataBus, Images
from .forms import PesanForm
from .models import Sewa

def index(req):
    # task = models.Pasien.objects.all()
    # return render(req, 'sewa/index.html')
    tampil = DataBus.objects.all()   
    return render(req,'sewa/index.html',{'tampil':tampil}) 

    
def detail(req, id):
    tampil = DataBus.objects.filter(pk=id)
    image = Images.objects.all()
    data = {
        'data':tampil,
        'image' : image,
    }   
    return render(req,'sewa/detail.html',data) 

def pesan(req):
    form = PesanForm(req.POST or None, req.FILES or None)
    if req.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect('index')
    return render(req, 'sewa/pesan.html',{
        'form': form,
    })
# def detail(req, id):
#     tampil = DataBus.objects.filter(pk=id)
#     image = Images.objects.all()
#     data = {
#         'data':tampil,
#         'image':image,
#     }   
#     return render(req, 'sewa/pesan.html',data)

def tambah(req):
    return render(req, 'sewa/tambah.html')

# def rinci(req):
#     return render(req, 'sewa/rinci.html')

# def Tambah(req):
#     if req.POST:
#         models.Sewa.objects.create(
#         nama_pemesan=req.POST['nama_pemesan'],
#         no_ktp=req.POST['no_ktp'],
#         alamat=req.POST['alamat'],
#         intstalasi=req.POST['intstalasi'],
#         jabatan=req.POST[' jabatan'],
#         no_hp=req.POST[' no_hp'], )
#         return redirect('/pengguna/user.html')
#     task = models.Sewa.objects.all()
#     return render(req, 'sewa/tambah.html',
#     { 'data' : task,
#     })