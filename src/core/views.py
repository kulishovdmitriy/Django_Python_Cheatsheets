from django.shortcuts import render # noqa

# Create your views here.


def home(request):
    return render(request, 'index.html')
