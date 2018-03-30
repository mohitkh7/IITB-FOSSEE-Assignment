"""Payment App URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from .views import index, TutorialList, payment_list

urlpatterns = [
    path('', index, name="home"),
    path('tutorial/', TutorialList.as_view(), name="home"),
    path('payment/<int:month>/<int:year>/', payment_list, name="payment_list"),
    path('tutorial/<int:month>/<int:year>/', TutorialList.as_view(), name="tutorial_list"),
]
