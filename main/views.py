from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html')  # adjust template path if needed

def post(request):
    return render(request, 'main/post_product.html')

def shop(request):
    return render(request, 'main/shop.html')

def login(request):
    return render(request, 'registration/login.html')    

def sign_up(request):
    return render(request, 'registration/sign_up.html')    