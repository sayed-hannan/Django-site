from django.urls import path
from . import views

app_name = 'insight'

urlpatterns = [
    path("insight/", views.newsletter_list, name='newsletter_list'),
    path('insight/<int:newsletter_id>/', views.newsletter_detail, name='newsletter_detail'),
    path('publish_newsletter/', views.publish_newsletter, name='publish_newsletter'),
    # url for form
    path('submit-form/', views.submit_form, name='submit_form'),
]

