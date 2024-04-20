from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Newsletter
from .forms import NewsletterForm  # Import your NewsletterForm
# In your other app's views.py
from nova.models import Subscription


def newsletter_list(request):
    # Get the most recent newsletter based on the publication date
    latest_newsletter = Newsletter.objects.latest('publication_date')

    # Exclude the latest newsletter and order the rest by publication date in descending order
    other_newsletters = Newsletter.objects.exclude(id=latest_newsletter.id).order_by('-publication_date')

    # Number of newsletters to display per page
    per_page = 16  # Adjust this value as needed

    # Create a Paginator instance for the other newsletters
    paginator = Paginator(other_newsletters, per_page)

    # Get the current page number from the request's GET parameters
    page = request.GET.get('page')

    try:
        # Get the other newsletters for the current page
        other_newsletters_page = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page
        other_newsletters_page = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver the last page of results
        other_newsletters_page = paginator.page(paginator.num_pages)

    context = {
        'latest_newsletter': latest_newsletter,
        'other_newsletters_page': other_newsletters_page,
    }

    return render(request, 'newsletter_list.html', context)


def newsletter_detail(request, newsletter_id):
    newsletter = get_object_or_404(Newsletter, pk=newsletter_id)

    context = {
        'newsletter': newsletter,
    }

    return render(request, 'newsletter_detail.html', context)


def publish_newsletter(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            
            # Create a new Newsletter instance and save it to the database
            newsletter = Newsletter(title=title, content=content)
            newsletter.save()
            
            # Redirect to the 'publish_newsletter' URL pattern within the 'insight' app
            return redirect('insight:publish_newsletter')
    else:
        form = NewsletterForm()

    return render(request, 'publish_newsletter.html', {'form': form})



# Subscrription form 
from django.http import JsonResponse

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
