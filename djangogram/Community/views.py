from django.shortcuts import render

# Create your views here.
def feed(request):
    return render(request, 'Community/feed.html')

def edit(request):
    return render(request, 'Community/edit.html')

def create(request):
    return render(request, 'Community/create.html')

