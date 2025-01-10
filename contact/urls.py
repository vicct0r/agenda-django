from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    path('', views.index, name='contact_home'),
    path('contato/', views.home, name='base_home'),
    path('search/', views.search, name='contact_search'),
    path('contato/criar/', views.create_contact, name='contact_create'),
    path('contato/<int:contact_id>/', views.detail, name='contact_detail'),
    path('contato/<int:contact_id>/update/', views.update_contact, name='contact_update'),
    path('contato/<int:contact_id>/delete/', views.delete_contact, name='contact_delete'),

    path('user/create/', views.register, name='register'),
]  