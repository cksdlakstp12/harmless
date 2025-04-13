"""harmless_cigarette URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # 홈페이지

    path('about/', views.company_introduction, name='company_introduction'),
    path('about/', views.vision, name='vision'),
    path('about/', views.people, name='people'),

    path('product/', views.product_introduction, name='product_introduction'),
    path('product/', views.purchase, name='purchase'),

    path('funding/', views.funding, name='funding'),
    path('funding/', views.go2fund, name='go2fund'),

    path('assistance/', views.customer_board, name='customer_board'),
    path('assistance/', views.review, name='review'),

    path('account/', views.login, name='login'),
    path('account/', views.mypage, name='mypage'),
    path('account/', views.signin, name='signin'),
]
