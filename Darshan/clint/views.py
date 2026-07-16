from django.shortcuts import render

# Create your views here.
def all_clint(request):
    return render(request, 'clint/all_clint.html')
