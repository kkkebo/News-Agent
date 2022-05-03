from django.http import HttpResponse
from django.shortcuts import render

from .models import News

def index(request):
    news = News.objects.order_by('-created_at')
    context = {
        'news': news,
        'title': 'News List'
    }
    return render(request, 'news/index.html', context)


