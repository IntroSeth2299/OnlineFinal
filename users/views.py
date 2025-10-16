
from django.shortcuts import render,redirect
from . models import User
from .forms import UserAddForm,UserEditForm

def user_list(request):
    u = User.objects.all()
    return render(request,"user/user_list.html",{"users":u})

def user_add(request):
    form = UserAddForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("user_list")
    return render(request,"user/user_add.html",{"form":form})

def user_edit(request, pk):
    u = User.objects.filter(pk = pk).first()
    form = UserEditForm(request.POST or None,instance=u)
    if form.is_valid():
        form.save()
        return redirect("user_list")
    return render(request,"user/user_edit.html",{"form":form})

def user_deleted(request,pk):
    u = User.objects.filter(pk = pk).first()
    if request.method == "POST":
        u.delete()
        return redirect("user_list")
    return render(request,"user/user_delete.html",{"user":u})

