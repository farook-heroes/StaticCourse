from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
  path('' , views.test,  name='test'),
  path('tables/', views.tables, name='tables'),
  path('calendar/', views.sample_page, name='sample_page'),
  path('tab/', views.tab_page, name='tab'),
  path("details/<str:username>",views.details,name="details")
]
