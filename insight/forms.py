from django import forms
from .models import Newsletter
from nova.models import Subscription as NovaSubscription
from nova.forms import SubscriptionForm as NovaSubscriptionForm


# for publishing coneten 
class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['title', 'content']

    content = forms.CharField(widget=forms.Textarea(attrs={'id': 'editor'}))



# Your newsletter app's SubscriptionForm can now inherit from NovaSubscriptionForm
class SubscriptionForm(NovaSubscriptionForm):
    class Meta:
        model = NovaSubscription
        fields = ['name', 'email', 'subscribe_news']