#coding: utf-8
from __future__ import unicode_literals
from this import s
from django.db import models


class ModelWeapon(models.Model):
    title = models.CharField(max_length=50, verbose_name='Модель оружия')
    ttc = models.TextField(verbose_name='Тактико-технические характеристики')
    history = models.TextField(verbose_name='История модели')

    class Meta:
        verbose_name = 'Модель оружия'
        verbose_name_plural = 'Модели оружия'

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/%d/" % self.id


class ManufacturerWeapon(models.Model):
    title = models.CharField(max_length=50, verbose_name='Производитель оружия')
    #country = models.ForeignKey(CountryFabricator, verbose_name='Страна производитель')

    class Meta:
        verbose_name = 'Приозводитель оружия'
        verbose_name_plural = 'Производители оружия'

    def __unicode__(self):
        return self.title


class CountryFabricator(models.Model):
    title = models.CharField(max_length=30, verbose_name='Страна')

    class Meta:
        verbose_name = 'Страна производитель'
        verbose_name_plural = 'Страны производители'

    def __unicode__(self):
        return self.title


class TypeWeapon(models.Model):
    title = models.CharField(max_length=30, verbose_name='Тип оружия')

    class Meta:
        verbose_name = 'Тип оружия'
        verbose_name_plural = 'Типы оружия'

    def __unicode__(self):
        return self.title

    def __getitem__(self):
        return self.title


class Patron(models.Model):
    title = models.CharField(max_length=50, verbose_name='Патрон по виду оружия')
    type_patron = models.CharField(max_length=50, verbose_name='Тип патрона')
    characteristic = models.TextField(verbose_name='Характеристика патрона')
    count = 7

    class Meta:
        verbose_name = 'Патрон'
        verbose_name_plural = 'Патроны'

    def __unicode__(self):
        return self.type_patron

    def get_absolute_url(self):
        return "/%g/" % self.id


class Weapon(models.Model):
    title = models.CharField(max_length=100, verbose_name='Тип оружия')
    model = models.ForeignKey(ModelWeapon, related_name='+', verbose_name='Модель оружия')
    mark = models.ForeignKey(ManufacturerWeapon, related_name='+', verbose_name='Производитель оружия')
    patron = models.ForeignKey(Patron, related_name='weapons', verbose_name='Патрон')
    country = models.ForeignKey(CountryFabricator, related_name='weapons', verbose_name='Страна производитель')
    history = models.ForeignKey(ModelWeapon, related_name='+', verbose_name='История модели')
    pub_date = models.DateTimeField()

    class Meta:
        verbose_name = 'Оружие'
        verbose_name_plural = 'Оружия'

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/cw/%i/" % self.id

    def get_url_history(self):
        return "/cw/%i/%d/" % (self.id, self.history.id)

    def get_url_patron(self):
        return "/cw/%i/p/%g/" % (self.id, self.patron.id)











