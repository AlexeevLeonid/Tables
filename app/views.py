from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.db.models import Count
from django.template import RequestContext

from .models import Title, Note



# получение данных из бд и отправка их в виде словаря таблица - QuerySet заметок
def home(request):

    titles = Title.objects.annotate(count=Count('note')).order_by('count')
    tables = {}
    for i in titles:
        tables[i] = Note.objects.filter(id_title=i)
    return render(request, "app/home.html", {"tables": tables})

def edit_title(request, id):
    titles = Title.objects.all()
    tables = {}
    for i in titles:
        tables[i] = Note.objects.filter(id_title=i)
    return render(request, "app/edit_title.html", {"tables": tables, "id": id})

def edit_note(request, id):
    table = Note.objects.get(id=id).id_title
    note_set = Note.objects.filter(id_title=table)
    return render(request, "app/edit_note.html", {"table": table, "note_set": note_set, "id": id})


#внесение в бд заметки в таблицу по пришедшему имени таблицы (если такой таблицы нет, создаётся новая)
def add_note(request):
    if request.method == "POST":
        title, created = Title.objects.get_or_create(name=request.POST.get("title_name"))
        title.save()
        title.note_set.create(text=request.POST.get("note"))
    return HttpResponseRedirect("/")


#добавление в точно существующую таблицу новой заметки
def add_row(request):
    if request.method == "POST":
        title = Title.objects.get(id=request.POST.get("table_id"))
        title.note_set.create(text=request.POST.get("note"))
    return HttpResponseRedirect("/")


#редактирование названия таблицы (если пришла пустая строка, удаление таблицы)
def edit_title_submit(request, id):
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


#редактирование заметки (если пришла пустая строка, удаление заметки)
def edit_note_submit(request, id):
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