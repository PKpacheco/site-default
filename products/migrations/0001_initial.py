# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-11-12 20:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'Nome ')),
                ('photo', models.ImageField(blank=True, null=True, upload_to=b'content/', verbose_name=b'Foto ')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
            },
        ),
    ]
