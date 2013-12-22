#coding: utf-8
from django.shortcuts import render
from dj_project.models import *
from django.views.generic import ListView, DetailView


class WeaponsListView(ListView):  # представление в виде списка
    model = Weapon  # модель для представления


class WeaponDetailView(DetailView):  # детализированное представление модели
    model = Weapon


class ModelWeaponDetailView(DetailView):  # детализированное представление модели
    model = ModelWeapon


class PatronDetailView(DetailView):
    model = Patron


class PatronListView(ListView):
    model = Patron



