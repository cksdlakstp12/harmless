from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'main/home.html')


def company_introduction(request):
    return render(request, 'about/introduction.html')

def vision(request):
    return render(request, 'about/vision.html')

def people(request):
    return render(request, 'about/people.html')


def product_introduction(request):
    return render(request, 'product/introduction.html')

def purchase(request):
    return render(request, 'product/purchase.html')


def funding(request):
    return render(request, 'funding/funding.html')

def go2fund(request):
    return render(request, 'funding/go2fund.html')


def customer_board(request):
    return render(request, 'assistance/customer_board.html')

def review(request):
    return render(request, 'assistance/review.html')


def login(request):
    return render(request, 'account/login.html')

def mypage(request):
    return render(request, 'account/mypage.html')

def signin(request):
    return render(request, 'account/signin.html')

