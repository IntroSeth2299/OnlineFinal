# employees/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_list, name='employee_list'),
    path('add/', views.employee_add, name='employee_add'),
    path('edit/<int:id>/', views.employee_edit, name='employee_edit'),
    path('delete/<int:id>/', views.employee_deleted, name='employee_delete'),
]
