from django.urls import path
from app import views
 
urlpatterns = [
    path('', views.index), #стартовая страница
    path('add_note/', views.add_note),#добавление заметки/таблицы
    path('add_row/', views.add_row),#добавление заметки
    path('edit_title/<int:id>/', views.edit_title),
    path('edit_title/<int:id>/submit/', views.edit_title_submit),#редактирование таблицы
    path('edit_note/<int:id>/', views.edit_note),#редактирование заметки
    path('edit_note/<int:id>/submit/', views.edit_note_submit),#редактирование заметки
]