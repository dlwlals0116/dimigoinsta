from django.db.models import Q
from django.shortcuts import render
from articleapp.models import Article


def search(request):
    articles = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        articles = Article.objects.all().filter(Q(title__contains=query) | Q(content__contains=query))

    return render(request, 'searchapp/search.html', {'query': query, 'articles': articles})
