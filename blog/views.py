from django.shortcuts import render
from django.views import genric
from . import models

# Create your views here.
def article_list(request):
    return render(request, "blog/article_list.html", {})