
from django.shortcuts import render,redirect
from . models import Tag
from .forms import TagAddForm,TagEditForm
from users.decorators import user_login_required

@user_login_required
def tag_list(request):
    t = Tag.objects.all()
    return render(request,"tag/tag_list.html",{"tags":t})
@user_login_required
def tag_add(request):
    form = TagAddForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("tag_list")
    return render(request,"tag/tag_add.html",{"form":form})
@user_login_required
def tag_edit(request, pk):
    t = Tag.objects.filter(pk = pk).first()
    form = TagEditForm(request.POST or None,instance=t)
    if form.is_valid():
        form.save()
        return redirect("tag_list")
    return render(request,"tag/tag_edit.html",{"form":form})
@user_login_required
def tag_deleted(request,pk):
    tag = Tag.objects.filter(pk = pk).first()
    if request.method == "POST":
        tag.delete()
        return redirect("tag_list")
    return render(request,"tag/tag_delete.html",{"tag":tag})

