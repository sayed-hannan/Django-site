from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from .models import Subscription, ContactFormSubmission
# from django.views.decorators.csrf import csrf_exempt
from django import forms 
from .forms import ContactForm
# Create your views here.
def index(request):
    return render(request, "index.html")



@csrf_protect  # For demonstration purposes only; CSRF should be handled properly
def submit_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subscribe_news = request.POST.get('subscribe-news') == 'on'  # Checkbox value

        # Create and save the subscription instance
        subscription = Subscription(name=name, email=email, subscribe_news=subscribe_news)
        subscription.save()

        response_data = {'success': True, 'message': 'Form submitted successfully!'}
        return JsonResponse(response_data)

    return JsonResponse({'success': False, 'message': 'Invalid request'}, status=400)


def contact(request):
    return render(request, 'contact.html')





import logging

logger = logging.getLogger(__name__)

@csrf_protect
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            response_data = {'success': True, 'message': 'Form submitted successfully!'}
            return JsonResponse(response_data)
        else:
            logger.error('Form data is not valid: %s', form.errors)
            response_data = {'success': False, 'message': 'Form data is not valid'}
            return JsonResponse(response_data, status=400)
    return JsonResponse({'success': False, 'message': 'Invalid request'}, status=400)