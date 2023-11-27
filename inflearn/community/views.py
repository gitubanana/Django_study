from django.shortcuts import render
from community.models import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

def write(request):
    if request.method == 'POST':
        Article.objects.create(
            name = request.POST['name'],
            title = request.POST['title'],
            contents = request.POST['contents'])

    return render(request, 'write.html')

def list(request):
    articleList = Article.objects.all()
    return render(request, 'list.html', {'articleList' : articleList})

def view(request, num='1'):
    article = Article.objects.get(id=num)
    return render(request, 'view.html', {'article' : article})

