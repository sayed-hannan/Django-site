from django.urls import path
from . import views

app_name = 'nova'
urlpatterns = [
    path("", views.index, name='index'),
    path('submit-form/', views.submit_form, name='submit_form'),
    path('contact/', views.contact, name='contact'),
        path('submit-contact/', views.contact_view, name='submit_contact'),
]
