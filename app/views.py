from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.template import RequestContext

from .models import Title, Note



# получение данных из бд
def index(request):
    titles = Title.objects.all()
    tables = {}
    for i in titles:
        tables[i] = Note.objects.filter(id_title=i)

    return render(request, "app/home.html", {"tables": tables})


def add_note(request):
    if request.method == "POST":
        title, created = Title.objects.get_or_create(name=request.POST.get("title_name"))
        title.save()
        title.note_set.create(text=request.POST.get("note"))
    return HttpResponseRedirect("/")


def add_row(request):
    if request.method == "POST":
        title = Title.objects.get(id=request.POST.get("table_id"))
        title.note_set.create(text=request.POST.get("note"))
    return HttpResponseRedirect("/")


def edit_title(request, id):
    try:
        title = Title.objects.get(id=id)
        if request.method == "POST":
            input = request.POST.get("text")
            if input == "":
                title.delete()
                return HttpResponseRedirect("/")
            else:
                title.name = request.POST.get("text")
                title.save()
                return HttpResponseRedirect("/")
        else:
            return render(request, "app/edit_title.html", {"title": title})
    except Title.DoesNotExist:
         return HttpResponseNotFound("<h2>Person not found</h2>")


def edit_note(request, id):
    try:
        note = Note.objects.get(id=id)
        if request.method == "POST":
            input = request.POST.get("text")
            if input == "":
                note.delete()
                return HttpResponseRedirect("/")
            else:
                note.text = request.POST.get("text")
                note.save()
                return HttpResponseRedirect("/")
        else:
            return render(request, "app/edit_title.html", {"note": note})
    except Title.DoesNotExist:
         return HttpResponseNotFound("<h2>Person not found</h2>")