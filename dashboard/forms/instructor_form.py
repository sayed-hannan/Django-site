from django import forms
from ..models import InstructorProfile

class InstructorProfileForm(forms.ModelForm):
    class Meta:
        model = InstructorProfile
        fields = ['bio', 'profile_picture']



