from django.urls import path
from . import views


urlpatterns = [
    path('',views.instructor_list,name="instructor_list"),
    path('add/',views.instructor_add,name="instructor_add"),
    path('edit/<int:pk>/',views.instructor_edit,name="instructor_edit"),
    path('delete/<int:pk>/',views.instructor_deleted,name="instructor_delete"),
]