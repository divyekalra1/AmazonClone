from django.shortcuts import render,redirect
from .forms import RegistrationForm
from django.contrib.auth.models import Group
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='customer')
            user.groups.add(group)
            return redirect("login")
    else:
        form = RegistrationForm()
    return render(request,'users/signup.html',{'form' : form, "title": "Register"})

