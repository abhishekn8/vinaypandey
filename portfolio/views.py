from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'portfolio/home.html')

def works(request):
    return render(request, 'portfolio/works.html')


def about(request):
    return render(request, 'portfolio/about.html')