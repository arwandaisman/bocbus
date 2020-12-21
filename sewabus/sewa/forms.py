
from .forms import *
from django import forms
from .models import Sewa

  
class PesanForm(forms.ModelForm): 
    class Meta: 
        model = Sewa
        fields = "__all__"

    # widgets = {
    #         'tanggal_mulai': AdminDateWidget()
    #     }

    # widgets ={
    #     'tanggal_mulai': 
        

    # }
