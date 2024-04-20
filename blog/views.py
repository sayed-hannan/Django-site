from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Article
from django.utils import timezone  # Import the timezone module
from .forms import ArticleForm



def article_list(request):
    now = timezone.now()  # Define the 'now' variable
    article_list = Article.objects.filter(publication_date__lte=now).order_by('-publication_date')
    paginator = Paginator(article_list, 20)  # Show 20 articles per page

    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        articles = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver the last page of results.
        articles = paginator.page(paginator.num_pages)

    return render(request, 'article_list.html', {'articles': articles})


def article_detail_view(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    context = {'article': article}
    return render(request, 'article_layout.html', context)


def publish_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()  # Save the article to the database
            return redirect('publish_article')  # Redirect to the article list view
    else:
        form = ArticleForm()

    return render(request, 'publish_article.html', {'form': form})
