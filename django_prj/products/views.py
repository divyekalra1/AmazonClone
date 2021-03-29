from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Product
from django.contrib.auth.models import User
from .forms import NewProduct
from django.contrib import messages
@login_required
def homepage(request):
    context = {
    'products' : Product.objects.all(),
    'title' : "Homepage"
    }
    return render(request,'products/homepage.html',context)


@login_required
def newProduct(request):
    form = NewProduct()
    if request.method == "POST":
        # user = request.user.username
        form = NewProduct(request.POST)
        form.instance.vendor = request.user

        # form.author = user
        if form.is_valid():
            form.save()
            return redirect('homepage')
        # else:
        #     messages.error(request,"Could not create product")
    context = {"form":form, "title":"New Product"}
    return render(request,'products/createProduct.html',context)
