from django.shortcuts import render
from employees.models import Employee
from students.models import Student
from lessons.models import Lesson
from enrollments.models import Enrollment,LessonProgress,Review
from tags.models import Tag
from instructors.models import Instructor
from categories.models import Category
from courses.models import Course
from users.models import User
from users.decorators import user_login_required

@user_login_required
def student_dashboard(request):
    student_count = Student.objects.count()
    lesson_count = Lesson.objects.count()
    enrollment_count = Enrollment.objects.count()
    lesson_progress_count = LessonProgress.objects.count()
    tag_count = Tag.objects.count()
    category_count = Category.objects.count()
    course_count = Course.objects.count()
    content = {
        "student_count": student_count,
        "lesson_count": lesson_count,
        "enrollment_count": enrollment_count,
        "lesson_progress_count": lesson_progress_count,
        "tag_count":tag_count,
        "category_count":category_count,
        "course_count":course_count,
    }
    
    return render(request,"student_dashboard/student_dashboard.html",content)