# coding: utf-8

from django.db import models
from core.models import TimeStampedModel


class Product(TimeStampedModel):
    name = models.CharField(max_length=255, verbose_name="Nome ")
    photo = models.ImageField(upload_to='content/', verbose_name='Foto ', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['name']
