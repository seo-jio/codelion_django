from django.shortcuts import render

# Create your views here.

def productlist(request):
    return render(request, 'productlist.html')

def firstproduct(request):
    return render(request, 'productfirst.html')