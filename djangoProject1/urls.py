from django.urls import path
from app import views
 
urlpatterns = [
    path('', views.index),
    path('add_note/', views.add_note),
    path('add_row/', views.add_row),
    path('edit_title/<int:id>/', views.edit_title),
    path('edit_note/<int:id>/', views.edit_note),

    # path('edit/<int:id>/', views.edit),
    # path('delete/<int:id>/', views.delete),
]