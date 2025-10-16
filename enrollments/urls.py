from django.urls import path
from . import views

urlpatterns = [

    path('', views.enrollment_list, name="enrollment_list"),
    path('add/', views.enrollment_add, name="enrollment_add"),
    path('edit/<int:pk>/', views.enrollment_edit, name="enrollment_edit"),
    path('delete/<int:pk>/', views.enrollment_deleted, name="enrollment_delete"),


    path('progress/', views.lesson_progress_list, name="lesson_progress_list"),
    path('progress/add/', views.lesson_progress_add, name="lesson_progress_add"),
    path('progress/edit/<int:pk>/', views.lesson_progress_edit, name="lesson_progress_edit"),
    path('progress/delete/<int:pk>/', views.lesson_progress_deleted, name="lesson_progress_delete"),


    path('reviews/', views.review_list, name="review_list"),
    path('reviews/add/', views.review_add, name="review_add"),
    path('reviews/edit/<int:pk>/', views.review_edit, name="review_edit"),
    path('reviews/delete/<int:pk>/', views.review_deleted, name="review_delete"),
]
