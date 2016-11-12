# coding: utf-8
from django.db import models

from core.models import TimeStampedModel


class Content(TimeStampedModel):
    photo = models.ImageField(upload_to='content/', verbose_name='Foto do conteudo', blank=True, null=True)
    text = models.CharField(max_length=255, verbose_name="Texto")
    subtitle = models.CharField(max_length=255, verbose_name="Legenda")

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Conteúdo'
        verbose_name_plural = 'Conteúdo'
