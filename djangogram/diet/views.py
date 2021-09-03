from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from djangogram.users.models import User as user_model


# Create your views here.
def diet(request):
    return render(request, 'diet.html')
