"""getproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views


urlpatterns = [
  # path('',views.blogsm, name='blogsm'),
  #path('blogs/',views.blogsmn, name='blogsmn'),
   path('news/',views.blogsm,name='blogsm'),
   path('post/<int:pk>',views.post, name='post'),
   path('cat/<int:idm>',views.cat, name='cate'),      
  # path('form/',views.form,name='formme'), 
   path('news/',views.blogsm, name='news'),
   path('',views.getnow,name='getnow'), 
   path('gallery/',views.gallery, name='uploaderget'),
   path('vaca/',views.vacancym,name='vacant'),
   path('topleader/',views.topleader,name='topleaderget'),  
   path('resource/',views.reso,name='resource'),
   path('plandoc/',views.planget,name='plandocs'),
   path('report/',views.report,name='report'),
   path('guide/',views.guide,name='guide'),
   path('rule/',views.rule,name='rule'),
   path('missionvision/',views.missionv,name='missionvision'),
   path('duitess/',views.duites,name='duites'),
   path('organ/',views.organ,name='organ'),
   path('bid/',views.bid,name='bid'), 
   path('service/',views.service,name='service'), 
   path('contact/',views.contact,name='contact'),
   path('videos/',views.videos,name='videos'),
   path('event/',views.event,name='event'),
   
   

]
