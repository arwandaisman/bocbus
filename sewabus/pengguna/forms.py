
from .forms import *
from django import forms
from .models import DataBus,Images, Ketersediaan
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
  
class BusForm(forms.ModelForm): 
   
    class Meta: 
        model = DataBus 
        exclude = ['po_id', 'judul','tambahan', 'ac','dvd', 'toilet','stop_kontak','sabuk_pengaman','bagasi', 'wifi', 'tv', 'bantal', 'selimut', 'smoking_area']
        # fields = "__all__"

    # widgets ={
    #     'kategori': forms.Select(
    #         attrs={
    #             'class':'form-control',
    #         }
    #     ),
        

    # }


class EditBusForm(forms.ModelForm): 
   
    class Meta: 
        model = DataBus 
        exclude = ['po_id', 'judul','tambahan', 'ac','dvd', 'toilet','stop_kontak','sabuk_pengaman','bagasi', 'wifi', 'tv', 'bantal', 'selimut', 'smoking_area']



class SediaForm(forms.ModelForm): 
   
    class Meta: 
        model = Ketersediaan 
        exclude = [
            'sedia',
            # 'tanggal_mulai',
            # 'tanggal_selesai'
            ]
