from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class  Meta:
        model = Article
        fields = ['title', 'content']
    
    # Use a standard Textarea widget for the content field
    widgets = {
        'content': forms.Textarea(attrs={'id': 'editor'}),
    }



    # content = forms.CharField(widget=forms.Textarea(attrs={'id': 'editor'}))
