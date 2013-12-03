#coding: utf-8
from django.db import models


class ModelWeapon(models.Model):
    title = models.CharField(max_length=30, verbose_name='Модель оружия')
    ttc = models.TextField(max_length=20000, verbose_name='Тактико-технические характеристики')
    history = models.TextField(verbose_name='История')

    class Meta:
        verbose_name = 'Модель оружия'
        verbose_name_plural = 'Модели оружия'

    def __unicode__(self):
        return self.title


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
    characteristic = models.CharField(max_length=200, verbose_name='Характеристика патрона')

    class Meta:
        verbose_name = 'Патрон'
        verbose_name_plural = 'Патроны'

    def __unicode__(self):
        return self.title


class Weapon(models.Model):
    title = models.CharField(max_length=50, verbose_name='Тип оружия')
    mark = models.ForeignKey(ManufacturerWeapon, related_name='manufacturer', verbose_name='Производитель оружия')
    model = models.ForeignKey(ModelWeapon, related_name='model', verbose_name='Модель оружия')
    patron = models.ForeignKey(Patron, related_name='patrons', verbose_name='Патрон')
    country = models.ForeignKey(CountryFabricator, related_name='countris', verbose_name='Страна производитель')
    history = models.ForeignKey(ModelWeapon, related_name='historis', verbose_name='История модели')

    class Meta:
        verbose_name = 'Оружие'
        verbose_name_plural = 'Оружия'

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/cw/%i/" % self.id