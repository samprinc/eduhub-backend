from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_dashboard, name='student_dashboard'),
    path('api/lessons/', views.lesson_list_api, name='lesson_list_api'),
    path('api/lessons/<int:lesson_id>/quiz/', views.quiz_questions_api, name='quiz_questions_api'),
]
