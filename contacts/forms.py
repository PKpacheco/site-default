# coding: utf-8
from django import forms
from .models import Contact
from django.forms import ModelForm


class ContactForm(ModelForm):

    class Meta:
        model = Contact
        fields = ('name', 'phone', 'phone2', 'state', 'city', 'photo',
                  'email', 'site', 'facebook', 'instagram', 'pinterest', 'slug', 'content')

        widgets = {
            'site': forms.TextInput(attrs={'placeholder': 'ex: http://www.abc.com.br '}),
            'sub_category': forms.TextInput(attrs={'placeholder': 'ex: Doces'}),
            'phone': forms.TextInput(attrs={'placeholder': 'ex: (21) 2222-9999'}),
            'phone2': forms.TextInput(attrs={'placeholder': 'ex: (21) 2222-9999'}),
            'email': forms.TextInput(attrs={'placeholder': 'ex: email@fornecedor.com.br'}),

            'facebook': forms.TextInput(attrs={'placeholder': 'ex: http://www.facebook.com/usuario'}),
            'instagram': forms.TextInput(attrs={'placeholder': 'ex: http://www.instagram.com/usuario'}),
            'pinterest': forms.TextInput(attrs={'placeholder': 'ex: http://www.pinterest.com.br/usuario '}),
            'slug': forms.TextInput(attrs={'placeholder': 'ex: nome-do-fornecedor '}),

        }
