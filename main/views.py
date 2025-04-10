from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'main/home.html')

def company_introduction(request):
    return render(request, 'about/company_introduction.html')

def vision(request):
    return render(request, 'about/vision.html')

def people(request):
    return render(request, 'about/people.html')

def product_introduction(request):
    return render(request, 'product/product_introduction.html')

def purchase(request):
    return render(request, 'product/purchase.html')

def innovation(request):
    return render(request, 'main/innovation.html')

def careers(request):
    return render(request, 'main/careers.html')

def contact(request):
    return render(request, 'main/contact.html')