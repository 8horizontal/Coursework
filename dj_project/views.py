#coding: utf-8
from django.shortcuts import render
from dj_project.models import *
from django.views.generic import ListView,DetailView

class PostsListView(ListView): # представление в виде списка
    model = Weapon                   # модель для представления

class PostDetailView(DetailView): # детализированное представление модели
    model = Weapon
