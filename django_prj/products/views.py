from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Product
from django.contrib.auth.models import User
from .forms import NewProduct
from django.contrib import messages
from .decorators import authorized

@login_required
def homepage(request):
    if request.user.is_staff:
        context = {
                    'products' : request.user.product_set.all(),
                    'title' : "Homepage"
                  }
    else:
        context = {
                    'products' : Product.objects.all(),
                    'title' : "Homepage"
                  }
    return render(request,'products/homepage.html',context)

@login_required
@authorized(allowed_users=['admin','vendor'])
def newProduct(request):
    form = NewProduct()
    if request.method == "POST":
        form = NewProduct(request.POST)
        form.instance.vendor = request.user
        if form.is_valid():
            form.save()
            return redirect('homepage')
        # else:
        #     messages.error(request,"Could not create product")
    context = {"form":form, "title":"New Product"}
    return render(request,'products/createProduct.html',context)

@login_required
@authorized(allowed_users=['admin','vendor'])
def updateProduct(request,pk):
    product = Product.objects.get(id = pk)
    form = NewProduct(instance=product)
    if request.method == "POST":
        form = NewProduct(request.POST,instance = product)
        if form.is_valid():
            form.save()
            return redirect('homepage')
        # else:
        #     messages.error(request,"Could not create product")
    context = {"form":form, "title":"Product Update","product":product}
    return render(request,'products/updateProduct.html',context)

def detailProduct(request,pk):
    product = Product.objects.get(id = pk)
    context = {"title":"Product Detail","product":product}
    return render(request,'products/infoProduct.html',context)

@login_required
@authorized(allowed_users=['admin','vendor'])
def deleteProduct(request,pk):
    product = Product.objects.get(id = pk)
    if request.method == "POST":
            product.delete()
            return redirect('homepage')
        # else:
        #     messages.error(request,"Could not create product")
    context = {"title":"Delete Product","product":product}
    return render(request,'products/deleteProduct.html',context)
