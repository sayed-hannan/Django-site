from django.urls import path
from . import views

app_name = 'course'
urlpatterns = [
    path("course-catalog/", views.catalog, name='course-catalog')

]
