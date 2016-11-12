# coding: utf-8
from django.contrib import admin
from .models import Contact
from .forms import ContactForm


@admin.register(Contact)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
    form = ContactForm
