from django.http import request
from django.shortcuts import redirect, render
from .models import Products
from django.contrib import auth
#import user for login ,reg
from django.contrib.auth.models import User
#import for search
from django.db.models import Q

# Create your views here.
def home(request):
    books=Products.objects.all()
    #for search
    if request.method=="POST":
        search=request.POST.get('search')
        print('search = ',search)
        result= Products.objects.filter(Q(product_name__icontains=search) | Q(author__icontains=search) | Q(publisher__icontains=search)| Q(amount__icontains=search))
        print('===========result ',result)
        context={
            'result':result,
        }
        return render(request,"books/home.html",context)
    
    # print('total books ',books)
    context={
        'books':books,
    }
    return render(request,"books/home.html",context)

def loginView(request):
    if request.method=='POST':
        user = auth.authenticate(
            username=request.POST['username'],
            password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('homepage')
        else:
            return render(request,'books/login.html',
            {'error':'username or password is incorrect'})
    else:
        return render(request,"books/login.html")    

def sign_up(request):
    if request.method=='POST':
        if request.POST['password']==request.POST['cpassword']:
            try:
                user=User.objects.get(username=request.POST['username']),
                return render(request,'books/sign_up.html',
                {'error':'username aleary available try another'})
            except User.DoesNotExist:
                user=User.objects.create_user(request.POST['username'], password=request.POST['password'])
                auth.login(request,user)
                return redirect('homepage')
    else:
        return render(request,"books/sign_up.html")    

def logout(request):
    if request.method=='POST':
        auth.logout(request)
    return redirect('homepage')