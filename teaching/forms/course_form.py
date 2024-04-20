# teaching/forms.py

from django import forms
from courses.models import Course, Skill, Instructor
# from django.contrib.formtools.wizard import FormWizard
from django.utils import timezone  # Import the timezone module

class TitleDescriptionForm(forms.Form):
    title = forms.CharField(max_length=200)
    description = forms.CharField(widget=forms.Textarea)


class DateDurationAboutForm(forms.Form):
    start_date = forms.DateField(initial=timezone.now().date())  # Set initial value to the current date
    duration_weeks = forms.IntegerField()
    about = forms.CharField(widget=forms.Textarea)

SKILLS_CHOICES = (
    ('skill1', 'Skill 1'),
    ('skill2', 'Skill 2'),
    # Add more skills as needed
)

class SkillsForm(forms.Form):
    skills = forms.MultipleChoiceField(choices=SKILLS_CHOICES, widget=forms.CheckboxSelectMultiple)

class InstructorForm(forms.Form):
    instructor = forms.ModelChoiceField(queryset=Instructor.objects.all())




