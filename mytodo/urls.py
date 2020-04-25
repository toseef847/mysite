from django.urls import path
from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.todo_list, name = 'todo_list'),
    path('<int:todo_id>', views.todo, name = 'todo'),
    path('create', views.create, name = 'create'),
    path('updateform/<int:todo_id>', views.updateform, name= 'updateform'),
    path('update/<int:todo_id>', views.update, name = 'update'),
    path('ConfirmDelete/<int:todo_id>', views.ConfirmDelete, name= 'ConfirmDelete'),
    path('delete/<int:todo_id>', views.delete, name = 'delete'),
]
