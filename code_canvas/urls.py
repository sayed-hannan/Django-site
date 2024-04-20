from django.urls import path
from . import views

urlpatterns = [
    path('code-canvas/', views.execute_code, name='execute_code'),
]
