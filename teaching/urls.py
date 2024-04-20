from django.urls import path
from .views import CourseWizardView

urlpatterns = [
    path('create-course/', CourseWizardView.as_view(), name='create_course_wizard'),
    # Add other URL patterns as needed
]
