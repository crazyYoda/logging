from django.shortcuts import render
from .models import New
import logging

logger = logging.getLogger(__name__)


def index(request):
    news = New.objects.all()
    return render(request, 'index.html')


def detail(request, slug):
    news = New.objects.all()
    new = New.objects.get(slug__iexact=slug)
    return render(request, 'details.html', context={'new': new, 'news': news})
