# blog/forms.py
from django.contrib import admin
from .models import  Article


# Register the models with the admin site


admin.site.register(Article) 