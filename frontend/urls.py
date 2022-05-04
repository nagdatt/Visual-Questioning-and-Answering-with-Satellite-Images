from django.urls import path

from . import views

urlpatterns = [
     path('', views.index, name='index'),
     path('about', views.about, name='about'),
     path('contact', views.contact, name='contact'),
     path('stats', views.stats, name='stats'),
     path('analysis',views.data_analysis_tool,name='analysis'),

]