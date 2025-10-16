from django.shortcuts import render
from employees.models import Employee
from users.decorators import user_login_required

@user_login_required
def employee_dashboard(request):
    employee_count = Employee.objects.count()
    content = {
        "employee_count": employee_count,
    }
    
    return render(request,"employee_dashboard/employee_dashboard.html",content)