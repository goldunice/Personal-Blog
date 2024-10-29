from django.shortcuts import render, get_object_or_404
from .models import Articles


def allArticles(request):
    all_articles = Articles.objects.order_by("-pub_date")
    return render(request, "blog/index.html", {"articles": all_articles})


def detail(request, article_id):
    article = get_object_or_404(Articles, pk=article_id)
    return render(request, "blog/detail.html", {"article": article})
