from django.shortcuts import render

# Create your views here.
def match(request):
    return render(request, 'match.html')