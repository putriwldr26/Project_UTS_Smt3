from django.shortcuts import render

# Create your views here.
def biografi(request):
    return render(request, 'indexbiografi.html')
