# coding: utf-8

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse as r, reverse_lazy
from django.views.generic import DeleteView


from contacts.forms import ContactForm
from contacts.models import Contact


def list_contact(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts/list_contacts.html', {'contacts': contacts})
