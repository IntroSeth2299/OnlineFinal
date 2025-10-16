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

def instructor_dashboard(request):
    lesson_count = Lesson.objects.count()
    tag_count = Tag.objects.count()
    instructor_count = Instructor.objects.count()
    category_count = Category.objects.count()
    course_count = Course.objects.count()
    review_count = Review.objects.count()
    lesson_progress_count = LessonProgress.objects.count()
    content = {
        "lesson_count": lesson_count,
        "tag_count":tag_count,
        "instructor_count":instructor_count,
        "category_count":category_count,
        "course_count":course_count,
        "review_count": review_count,
        "lesson_progress_count" :lesson_progress_count ,
    }
    
    return render(request,"instructor_dashboard/instructor_dashboard.html",content)