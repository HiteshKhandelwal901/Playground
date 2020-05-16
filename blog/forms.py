from django import forms

class test_Form(forms.Form):
    first_name = forms.CharField(max_length = 200) 
    last_name = forms.CharField(max_length = 200) 
  