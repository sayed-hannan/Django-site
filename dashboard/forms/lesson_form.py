from django import forms
from courses.models import Lesson  # Import your Lesson model

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['title', 'module', 'lesson_type', 'content']

    # You can customize form field widgets, labels, etc., if needed.
    widgets = {
        'title': forms.TextInput(attrs={'class': 'form-control'}),
        'module': forms.Select(attrs={'class': 'form-control'}),
        'lesson_type': forms.Select(attrs={'class': 'form-control'}),
        'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
    }

    # You can also add custom validation or additional behavior here if needed.
