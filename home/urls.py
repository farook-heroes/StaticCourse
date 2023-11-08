from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
  path('home/' , views.index,  name='index'),
   path('contact/' , views.contact,  name='contact'),
  path('', views.test,  name='test'),
  path('tables/', views.tables, name='tables'),
  path('calendar/', views.sample_page, name='sample_page'),
  path('tab/', views.tab_page, name='tab'),
  path("details/<str:username>",views.details,name="details"),
    path('forms/form-elements/', views.form_elements, name='form_elements'),
]
