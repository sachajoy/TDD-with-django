from django.http.request import HttpRequest
from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    return render(request, 'home.html', {
        'new_item_next': request.POST.get('item_text', '')
    })