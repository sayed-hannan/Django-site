from django.shortcuts import render

# Create your views here.
from django.db import models
from django.shortcuts import render
from django.http import JsonResponse

# Create your models here.


# Create your views here.
from .models import Course

def catalogue(request):
    courses = Course.objects.all()
    return render(request, 'catalogue.html', {'courses': courses})


def course_intro(request, course_id):
    course = Course.objects.get(pk=course_id)  # Retrieve the course based on its ID
    return render(request, 'course_intro.html', {'course': course})