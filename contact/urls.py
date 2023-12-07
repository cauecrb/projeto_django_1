from django.urls import path
from contact import views

app_name = 'contact'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),

    #contact CRUD
    path('contato/<int:contact_id>/info/', views.contact, name='contact'),
    path('contato/create/', views.create, name='create'),
    path('contatp/<int:contact_id>/update/', views.update, name='update'),
    path('contatp/<int:contact_id>/delete/', views.delete, name='delete'),
]
