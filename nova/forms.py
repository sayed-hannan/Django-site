# forms.py
from django import forms
from .models import Subscription
from .models import ContactFormSubmission

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['name', 'email', 'subscribe_news',]


# Contact form
class ContactForm(forms.ModelForm):
    # Define choices for the 'category' field
    # CATEGORY_CHOICES = [
    #     ('feedback', 'Feedback / Questions about our online courses'),
    #     ('speaking', 'Speaking engagement for Andrew Ng'),
    #     ('press', 'Press or interview request'),
    #     ('entrepreneurship', 'Entrepreneurship or career advice'),
    #     ('other', 'Other'),
    # ]

    # category = forms.ChoiceField(choices=CATEGORY_CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = ContactFormSubmission
        fields = ['first_name', 'last_name', 'email', 'message']