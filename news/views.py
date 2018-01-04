from django.shortcuts import render
# from django.template import loader
from django.http import HttpResponse
from .models import Article
# Create your views here.

def index(request):
    return HttpResponse("Hello, world. This is index page")

def year_archive(request, year):
    a_list = Article.objcets.filter(put_date__year=year)
    context = {'year': year, 'article_list': a_list}
    return render(request, 'news/year_archive.html', context)