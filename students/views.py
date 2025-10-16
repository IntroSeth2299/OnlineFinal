
from django.shortcuts import render,redirect
from . models import Student
from .forms import StudentAddForm,StudentEditForm
from users.decorators import user_login_required
@user_login_required
def student_list(request):
    stu = Student.objects.all()
    return render(request,"student/student_list.html",{"students":stu})
@user_login_required
def student_add(request):
    form = StudentAddForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("student_list")
    return render(request,"student/student_add.html",{"form":form})
@user_login_required
def student_edit(request, pk):
    stu = Student.objects.filter(pk = pk).first()
    form = StudentEditForm(request.POST or None,instance=stu)
    if form.is_valid():
        form.save()
        return redirect("student_list")
    return render(request,"student/student_edit.html",{"form":form})
@user_login_required
def student_deleted(request,pk):
    stu = Student.objects.filter(pk = pk).first()
    if request.method == "POST":
        stu.delete()
        return redirect("student_list")
    return render(request,"student/student_delete.html",{"student":stu})

