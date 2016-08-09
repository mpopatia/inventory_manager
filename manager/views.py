from django.shortcuts import render
from django.http import HttpResponse

import json

# Create your views here.

def index(request):
    return render(request, 'manager/index.html', {})

def get_items(request):
    result = [{'name': 'A/C 250 X 350', 'quantity': 500}, {'name': 'B/C 150 X 750', 'quantity': 300}, {'name': 'F/C 350 X 150', 'quantity': 250}]
    return HttpResponse(json.dumps(result), content_type = "application/json")