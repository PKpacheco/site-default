# coding: utf-8
from datetime import datetime
from django.db import models

from core.models import TimeStampedModel


class Contact(TimeStampedModel):

    name = models.CharField(max_length=255, verbose_name="Nome do Fornecedor")
    phone = models.CharField(max_length=30, verbose_name="Telefone")
    phone2 = models.CharField(max_length=30, verbose_name="Telefone 2", blank=True, null=True)

    city = models.CharField(max_length=30, verbose_name="Cidade")
    state = models.CharField(max_length=255, verbose_name="Estado")
    photo = models.ImageField(upload_to='providers/', verbose_name='Foto do fornecedor', blank=True, null=True)

    email = models.EmailField(verbose_name="Email", blank=True, null=True)
    site = models.URLField(max_length=255, verbose_name="Site", blank=True, null=True)
    facebook = models.URLField(max_length=255, verbose_name="Facebook", blank=True, null=True)
    instagram = models.URLField(max_length=255, verbose_name="Instagram", blank=True, null=True)
    content = models.TextField(verbose_name="Conteudo", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Contato '
        verbose_name_plural = 'Contato'
        ordering = ['name']
