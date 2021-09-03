from django.shortcuts import render

# Create your views here.

def start(request):
    return render(request, 'exercise/start.html')

def playlist(request):
    return render(request, 'exercise/playlist.html')

def routine(request):
    return render(request, 'exercise/routine.html')
