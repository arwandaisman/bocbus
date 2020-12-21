
from .forms import *
from django import forms
from .models import DataBus,Images
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
  
class BusForm(forms.ModelForm): 
   
    class Meta: 
        model = DataBus 
        exclude = ['po_id']
        # fields = "__all__"

    # widgets ={
    #     'kategori': forms.Select(
    #         attrs={
    #             'class':'form-control',
    #         }
    #     ),
        

    # }
