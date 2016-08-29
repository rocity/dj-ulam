from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):

    return render(request, 'create.html', {
        'title_text': request.POST.get('title_text', '')
        })
