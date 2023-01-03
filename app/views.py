from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'a':200,'b':50,'c':40}
    return render(request,'conditions.html',d)