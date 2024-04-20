# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.article_list, name='article_list'),
    path('blog/<int:article_id>/', views.article_detail_view, name='article_layout'),
    path('publish_article/', views.publish_article, name='publish_article'),
]
