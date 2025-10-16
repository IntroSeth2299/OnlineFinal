from django.urls import path
from . import views


urlpatterns = [
    path('',views.tag_list,name="tag_list"),
    path('add/',views.tag_add,name="tag_add"),
    path('edit/<int:pk>/',views.tag_edit,name="tag_edit"),
    path('delete/<int:pk>/',views.tag_deleted,name="tag_delete"),
]