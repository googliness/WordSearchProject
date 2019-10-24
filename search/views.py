from django.http import HttpResponse
from django.shortcuts import render
from .utilities import getWordsWith
import json

def index(request):
    return render(request, 'index.html')


def search(request):
    prefix = request.GET.get('word', '')
    return HttpResponse(json.dumps(getWordsWith(prefix.lower())), 'application/json')
