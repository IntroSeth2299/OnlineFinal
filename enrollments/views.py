
from django.shortcuts import render,redirect
from . models import Enrollment
from .forms import EnrollmentAddForm,EnrollmentEditForm
from users.decorators import user_login_required
@user_login_required
def enrollment_list(request):
    enr = Enrollment.objects.all()
    return render(request,"enrollment/enrollment_list.html",{"enrollments":enr})
@user_login_required
def enrollment_add(request):
    form = EnrollmentAddForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("enrollment_list")
    return render(request,"enrollment/enrollment_add.html",{"form":form})
@user_login_required
def enrollment_edit(request, pk):
    enr = Enrollment.objects.filter(pk = pk).first()
    form = EnrollmentEditForm(request.POST or None,instance=enr)
    if form.is_valid():
        form.save()
        return redirect("enrollment_list")
    return render(request,"enrollment/enrollment_edit.html",{"form":form})
@user_login_required
def enrollment_deleted(request,pk):
    enr = Enrollment.objects.filter(pk = pk).first()
    if request.method == "POST":
        enr.delete()
        return redirect("enrollment_list")
    return render(request,"enrollment/enrollment_delete.html",{"enrollment":enr})

#Review

from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewAddForm, ReviewEditForm
@user_login_required
def review_list(request):
    reviews = Review.objects.all()
    return render(request, "review/review_list.html", {"reviews": reviews})
@user_login_required
def review_add(request):
    form = ReviewAddForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("review_list")
    return render(request, "review/review_add.html", {"form": form})
@user_login_required
def review_edit(request, pk):
    review = Review.objects.filter(pk=pk).first()
    form = ReviewEditForm(request.POST or None, instance=review)
    if form.is_valid():
        form.save()
        return redirect("review_list")
    return render(request, "review/review_edit.html", {"form": form})
@user_login_required
def review_deleted(request, pk):
    review = Review.objects.filter(pk=pk).first()
    if request.method == "POST":
        review.delete()
        return redirect("review_list")
    return render(request, "review/review_delete.html", {"review": review})



#Lesson Progress
from django.shortcuts import render,redirect
from . models import LessonProgress
from .forms import LessonProgressAddForm,LessonProgressEditForm
@user_login_required
def lesson_progress_list(request):
    lp = LessonProgress.objects.all()
    return render(request,"lesson_progress/lesson_progress_list.html",{"lesson_progresses":lp})
@user_login_required
def lesson_progress_add(request):
    form = LessonProgressAddForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("lesson_progress_list")
    return render(request,"lesson_progress/lesson_progress_add.html",{"form":form})
@user_login_required
def lesson_progress_edit(request, pk):
    lp = LessonProgress.objects.filter(pk = pk).first()
    form = LessonProgressEditForm(request.POST or None,instance=lp)
    if form.is_valid():
        form.save()
        return redirect("lesson_progress_list")
    return render(request,"lesson_progress/lesson_progress_edit.html",{"form":form})
@user_login_required
def lesson_progress_deleted(request,pk):
    rew = Review.objects.filter(pk = pk).first()
    if request.method == "POST":
        rew.delete()
        return redirect("lesson_progress_list")
    return render(request,"lesson_progress/lesson_progress_delete.html",{"lesson_progress":rew})