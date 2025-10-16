
from django.shortcuts import render,redirect
from . models import Lesson
from .forms import LessonAddForm,LessonEditForm
from users.decorators import user_login_required
@user_login_required
def lesson_list(request):
    les = Lesson.objects.all()
    return render(request,"lesson/lesson_list.html",{"lessons":les})
@user_login_required
def lesson_add(request):
    form = LessonAddForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("lesson_list")
    return render(request,"lesson/lesson_add.html",{"form":form})
@user_login_required
def lesson_edit(request, pk):
    less = Lesson.objects.filter(pk = pk).first()
    form = LessonEditForm(request.POST or None,instance=less)
    if form.is_valid():
        form.save()
        return redirect("lesson_list")
    return render(request,"lesson/lesson_edit.html",{"form":form})
@user_login_required
def lesson_deleted(request,pk):
    less = Lesson.objects.filter(pk = pk).first()
    if request.method == "POST":
        less.delete()
        return redirect("lesson_list")
    return render(request,"lesson/lesson_delete.html",{"lesson":less})

