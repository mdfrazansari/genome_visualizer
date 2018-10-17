# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 19:45:55 2018

@author: fraz
"""

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
#-----------start---------------
    path('cv1', views.cv1, name='cv1'),


#----------end------------------               
               
               
               
    path('', views.index, name='index'),
    path('vv2/', views.vv2, name='vv2'),
    path('f2_data/', views.f2_data, name='f2_data'),
    path('band_zoom/', views.bandZoom, name='bandZoom'),
    path('test1/', views.test1, name='test1'),
#----------genome visualizer---------------------#
    path('allChromosomeVariations/', views.allChromosomeVariations, name='allChromosomeVariations'),
    path('v1/', views.v1, name='v1'),
    path('v2/', views.v2, name='v2'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)