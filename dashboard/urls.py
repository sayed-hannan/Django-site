from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/instructor-profile/', views.Instructor, name='Instructor_profile'),
    path('dashboard/create-course/', views.create_course, name='create_course'),
    path('dashboard/create-course/create-lesson', views.create_lesson, name='create_lesson'),  # Moved this line up
   # Add more URL patterns for course creation, management, etc.
]
