from django.urls import path
from . import views

app_name = 'courses'
urlpatterns = [
    path("courses/", views.catalogue, name='catalogue'),
    path('course/intro/<int:course_id>/', views.course_intro, name='course_intro'),
]
