from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, 'home.html')


def coverage(request):
	return render(request, 'coverage.html')


def plans(request):
	return render(request, 'plans.html')


def why_insurance(request):
	return render(request, 'why_insurance.html')


def how_it_works(request):
	return render(request, 'how_it_works.html')


def member_support(request):
	return render(request, 'member_support.html')


def login_view(request):
	return render(request, 'login.html')


def register(request):
	return render(request, 'register.html')