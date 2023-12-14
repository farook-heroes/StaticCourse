from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
  path('home/' , views.index,  name='index'),
   path('teacher/' , views.teachers,  name='teacher'),
    path('student/' , views.student,  name='student'),
   path('contact/' , views.contact,  name='contact'),
    path('test-email/', views.test_email, name='test_email'),
     path('sample-page/', views.sample_page, name='sample_page'),
  path('', views.test,  name='test'),
  path('tables/', views.tables, name='tables'),
  path('calendar/', views.sample_page, name='sample_page'),
  path('tab/', views.tab_page, name='tab'),
  path("details/<str:username>",views.details,name="details"),
    path('forms/form-elements/', views.form_elements, name='form_elements'),
      path('profile/', views.profile, name='profile'),
]
