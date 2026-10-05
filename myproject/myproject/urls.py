"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from myapp.views import coverage, home, how_it_works, login_view, member_support, plans, register, why_insurance


urlpatterns = [
    path('', home, name='home'),
    path('coverage/', coverage, name='coverage'),
    path('plans/', plans, name='plans'),
    path('why-health-insurance/', why_insurance, name='why_insurance'),
    path('how-it-works/', how_it_works, name='how_it_works'),
    path('member-support/', member_support, name='member_support'),
    path('login/', login_view, name='login'),
    path('register/', register, name='register'),
    path('admin/', admin.site.urls),
]
