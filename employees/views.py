
from django.shortcuts import render,redirect
from . models import Employee
from .forms import EmployeeAddForm,EmployeeEditForm
from users.decorators import user_login_required
@user_login_required
def employee_list(request):
    emp = Employee.objects.all()
    return render(request,"employee/employee_list.html",{"employees":emp})
@user_login_required
def employee_add(request):
    form = EmployeeAddForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("employee_list")
    return render(request,"employee/employee_add.html",{"form":form})
@user_login_required
def employee_edit(request, pk):
    emp = Employee.objects.filter(pk = pk).first()
    form = EmployeeEditForm(request.POST or None,instance=emp)
    if form.is_valid():
        form.save()
        return redirect("employee_list")
    return render(request,"employee/employee_edit.html",{"form":form})
@user_login_required
def employee_deleted(request,pk):
    emp = Employee.objects.filter(pk = pk).first()
    if request.method == "POST":
        emp.delete()
        return redirect("employee_list")
    return render(request,"employee/employee_delete.html",{"employee":emp})

