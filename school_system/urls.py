"""
URL configuration for school_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from employees import urls as employee_url
from students import urls as student_url
from enrollments import urls as enrollment_url
from users import urls as user_url
from instructors import urls as instructor_url
from courses import urls as course_url
from lessons import urls as lesson_url
from tags import urls as tag_url
from categories import urls as category_url
from dashbaord import urls as dashboard_url
from account import urls as account_urls
from dashboard_instructor import urls as das_instructor_url
from dashboard_student import urls as das_student_url
from dashboard_employee import urls as das_employee_url
urlpatterns = [
    path('admin/', admin.site.urls),
    path('employees/', include(employee_url)),
    path('students/', include(student_url)),
    path('enrollments/', include(enrollment_url)),  # make sure trailing slash is here
    path('users/', include(user_url)),
    path('instructors/', include(instructor_url)),
    path('courses/', include(course_url)),
    path('lessons/', include(lesson_url)),
    path('tags/', include(tag_url)),
    path('categories/', include(category_url)),
    path('', include(dashboard_url)),
    path('',include(account_urls)),
    path('dashboard_instructors/',include(das_instructor_url)),
    path('dashboard_students/',include(das_student_url)),
    path('dashboard_employees/',include(das_employee_url)),


    # No need to include lesson_progress and reviews separately
    # They are already included inside enrollments/urls.py with paths like:
    # 'progress/' and 'reviews/'
]
