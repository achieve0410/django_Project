from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'myProject/index.html')

def index2(request):
    return render(request, 'myProject/index2.html')
