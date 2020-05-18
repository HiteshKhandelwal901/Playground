from django import forms
from .models import test_form_model

class test_Form(forms.ModelForm):
    #first_name = forms.CharField(max_length = 200) 
    #last_name = forms.CharField(max_length = 200) 
    class Meta: 
        model = test_form_model
        fields = "__all__"
  