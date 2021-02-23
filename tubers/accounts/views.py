from django.shortcuts import render

# Create your views here.
 
def login(request):
    return render(request, 'accounts/login.html')

def register(request):
    pass

def logout_user(request):
    pass

def dashbord(request):
    pass