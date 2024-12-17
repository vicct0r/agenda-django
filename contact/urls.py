from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    path('', views.home, name='base_home'),
    path('contato/', views.index, name='contact_home'),
    path('contato/<int:contact_id>/', views.detail, name='contact_detail'),
    path('search/', views.search, name='contact_search')
]  