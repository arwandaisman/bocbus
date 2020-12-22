from django.shortcuts import render, redirect, get_object_or_404
from . import models
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import BusForm
from .models import DataBus, Images
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

def edit(request,id):
    context ={}
    obj = get_object_or_404(DataBus, id = id)
    form = BusForm(request.POST or None, instance = obj)
    if form.is_valid(): 
        form.save() 
        return redirect('index')
    context["form"] = form
    return render(request, "pengguna/edit.html", context)


def user(request): 
    # tasks = DataBus.objects.filter(po_id=request.user)
    # form = BusForm()
    # if request.POST:
    #     form = BusForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         image = form.instance
    #         form.instance.po_id = request.user
    #         form.save()
    #         messages.success(request, 'Data telah ditambahkan.')
    #     return redirect('user')
        
    # return render(request, 'pengguna/user.html',{
    #     'form': form,
    #     'data': tasks,
    # })
    # idgb = DataBus.objects.filter(t_id=id)
    ImageFormSet = modelformset_factory(Images, fields = ('image',), extra=4)
    if request.method == 'POST':
        formx = BusForm(request.POST)
        print(request.POST)
        formset = ImageFormSet(request.POST or None, request.FILES or None)
        if formx.is_valid() and formset.is_valid():
            post = formx.save(commit=False)
            post.po_id = request.user
            post.judul= request.POST.get('judul')
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
        'formx': formx, 
        'formset': formset
    }
    return render(request, 'pengguna/user.html', context)

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
