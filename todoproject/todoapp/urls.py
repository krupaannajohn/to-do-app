from django.urls import path
from . import views
app_name = 'todoapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('todo/', views.todoappView, name='todo'),
    path('addTodoItem/',views.addTodoView), 
    path('todo/edit/<int:id>/', views.editTodoView, name='edit_todo'),
    path('deleteTodoItem/<int:id>/', views.deleteTodoView), 
] 