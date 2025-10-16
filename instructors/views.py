
from django.shortcuts import render,redirect
from . models import Instructor
from .forms import InstructorAddForm,InstructorEditForm
from users.decorators import user_login_required
@user_login_required
def instructor_list(request):
    ins = Instructor.objects.all()
    return render(request,"instructor/instructor_list.html",{"instructors":ins})
@user_login_required
def instructor_add(request):
    form = InstructorAddForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("instructor_list")
    return render(request,"instructor/instructor_add.html",{"form":form})
@user_login_required
def instructor_edit(request, pk):
    ins = Instructor.objects.filter(pk = pk).first()
    form =InstructorEditForm(request.POST or None,instance=ins)
    if form.is_valid():
        form.save()
        return redirect("instructor_list")
    return render(request,"instructor/instructor_edit.html",{"form":form})
@user_login_required
def instructor_deleted(request,pk):
    ins =Instructor.objects.filter(pk = pk).first()
    if request.method == "POST":
        ins.delete()
        return redirect("instructor_list")
    return render(request,"instructor/instructor_delete.html",{"instructor":ins})

