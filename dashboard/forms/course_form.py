from django import forms
from courses.models import Course, Module
from .module_form import ModuleForm
from django.forms import inlineformset_factory


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

ModuleFormSet = inlineformset_factory(Course, Module, form=ModuleForm, extra=1)
