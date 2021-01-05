from django.shortcuts import render, redirect, get_object_or_404
from . import models
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import BusForm, BusForm2, EditBusForm, BiayaBusForm
from .models import DataBus, Images, Biaya
from django.forms import modelformset_factory
from sewa.models import Sewa



# Create your views here.
@login_required(login_url=settings.LOGIN_URL)
def index (request):
    
    tampil = models.DataBus.objects.filter(po_id=request.user)
    data = {
        'data':tampil,
    }   
    return render(request,'pengguna/index.html',data)  
    
def detail(request, id):
    tampil = models.DataBus.objects.filter(pk=id).first()
    image = tampil.images.all()
    timage = models.Images.objects.filter(id=9).first()
    data = {
        'data':tampil,
        'image' : image,
        'timg' : timage,
    }   
    return render(request,'pengguna/detail.html',data) 

def edit(request, id):
    edt = models.DataBus.objects.get(id=id)
    # tampil = models.DataBus.objects.filter(pk=id).first()
    if request.POST:
        form = EditBusForm(request.POST, instance=edt)
        if form.is_valid():
            form.save()

            edt.judul= request.POST.get('judul')
            edt.ac= request.POST.get('ac')
            edt.dvd= request.POST.get('dvd')
            edt.toilet= request.POST.get('toilet')
            edt.stop_kontak= request.POST.get('stop_kontak')
            edt.sabuk_pengaman= request.POST.get('sabuk_pengaman')
            edt.bagasi= request.POST.get('bagasi')
            edt.wifi= request.POST.get('wifi')
            edt.tv= request.POST.get('tv')
            edt.bantal= request.POST.get('bantal')
            edt.selimut= request.POST.get('selimut')
            edt.smoking_area= request.POST.get('smoking_area')
            edt.tambahan= request.POST.get('tambahan')
            edt.save()
            return redirect('index')
    else:
        form = EditBusForm(instance=edt)
        konteks = {
            'form':form,
            'edt':edt
        }
    return render(request, "pengguna/edit.html", konteks)

# def edit(request,id):
#     context ={}
#     obj = get_object_or_404(DataBus, id = id)
#     form = EditBusForm(request.POST or None, instance = obj)
#     if form.is_valid(): 
#         form.save() 
#         return redirect('index')
#     context["form"] = form
#     return render(request, "pengguna/edit.html", context)

def fasilitas(request,id):
    tampil = models.Databus.objects.filter(pk=id).first()
    obj = models.Databus.objects.get(id=id)
    if request.method == 'POST' :
        if form.is_valid():
            form = BusForm2(request.POST, instance=obj)
            post.judul= request.POST.get('judul')
            post.ac= request.POST.get('ac')
            post.dvd= request.POST.get('dvd')
            post.toilet= request.POST.get('toilet')
            post.stop_kontak= request.POST.get('stop_kontak')
            post.sabuk_pengaman= request.POST.get('sabuk_pengaman')
            post.bagasi= request.POST.get('bagasi')
            post.wifi= request.POST.get('wifi')
            post.tv= request.POST.get('tv')
            post.bantal= request.POST.get('bantal')
            post.selimut= request.POST.get('selimut')
            post.smoking_area= request.POST.get('smoking_area')
            post.tambahan= request.POST.get('tambahan')
            form.save()
            return redirect('index')
    else:
        form = BusForm2()
    context = {
        'tampil': tampil,
        'form': form,
    }
    return render(request, "pengguna/fasilitas.html", context)


def user(request): 
    ImageFormSet = modelformset_factory(Images, fields = ('image',), extra=4)
    # tampil = models.DataBus.objects.filter(pk=id).first()
    if request.method == 'POST':
        formx = BusForm(request.POST)
        print(request.POST)
        formset = ImageFormSet(request.POST or None, request.FILES or None)
        if formx.is_valid() and formset.is_valid():
            post = formx.save(commit=False)
            post.po_id = request.user
            post.judul= request.POST.get('judul')
            post.ac= request.POST.get('ac')
            post.dvd= request.POST.get('dvd')
            post.toilet= request.POST.get('toilet')
            post.stop_kontak= request.POST.get('stop_kontak')
            post.sabuk_pengaman= request.POST.get('sabuk_pengaman')
            post.bagasi= request.POST.get('bagasi')
            post.wifi= request.POST.get('wifi')
            post.tv= request.POST.get('tv')
            post.bantal= request.POST.get('bantal')
            post.selimut= request.POST.get('selimut')
            post.smoking_area= request.POST.get('smoking_area')
            post.tambahan= request.POST.get('tambahan')
            # post.tanggal= request.POST.get('tanggal')
            post.save()


            for form in formset:
                try:
                    # image = form['image']
                    photo = Images(post=post, image=form.cleaned_data['image'])
                    # photo.t_id = Databus.id
                    photo.save()
                    
                except Exception as e:
                    break
        return redirect('index')
    else:
        formx = BusForm()
        formset = ImageFormSet(queryset=Images.objects.none())

    context = {
        # 'data':tampil,
        'formx': formx, 
        'formset': formset
    }
    return render(request, 'pengguna/user.html', context)


def biaya(request):
    if request.method == 'POST' :
        form = BiayaBusForm(request.POST)
        form.save()
        return redirect('index')
    else:
        form = BiayaBusForm()
    context = {
        'form': form,
    }
    return render(request, "pengguna/harga.html", context)

def harga (request):
    return render(request, 'pengguna/harga.html')


def profil (request):
    return render(request, 'pengguna/profil.html')


def hapus(request, id):
    konteks = {}
    tampil = models.DataBus.objects.filter(pk=id).delete()
    return redirect('index')

def tabel (request):
    tampil = Sewa.objects.all()
    data = {
        'data':tampil,
    }   
    return render(request,'pengguna/tabel.html',data)  

def icon (request):
   
    return render(request, 'pengguna/icon.html')


def typo (request):
   
    return render(request, 'pengguna/typo.html')
