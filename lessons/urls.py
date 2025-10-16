from django.urls import path
from . import views


urlpatterns = [
    path('',views.lesson_list,name="lesson_list"),
    path('add/',views.lesson_add,name="lesson_add"),
    path('edit/<int:pk>/',views.lesson_edit,name="lesson_edit"),
    path('delete/<int:pk>/',views.lesson_deleted,name="lesson_delete"),
]