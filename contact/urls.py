from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    path('', views.index, name='contact_home'),
    path('search/', views.search, name='contact_search'),
    path('contato/', views.home, name='base_home'),
    path('contato/criar/', views.create_contact, name='contact_create'),
    path('contato/<int:contact_id>/', views.detail, name='contact_detail'),
    path('contato/<int:contact_id>/update/', views.update_contact, name='contact_update'),
    path('contato/<int:contact_id>/delete/', views.delete_contact, name='contact_delete'),

    path('user/create/', views.register, name='register'),
    path('user/login/', views.login_view, name='login'),
    path('user/logout/', views.logout_view, name='logout'),
    path('user/update/', views.user_update, name='user_update')
    
]  