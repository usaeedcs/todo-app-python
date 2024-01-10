from django.contrib import admin
from django.urls import path
from .views import home, login, signup, logout, add_todo, update_todo, delete_todo

# Defining URL patterns here

urlpatterns = [
    path('', home, name="home"),
    path('login/', login, name="login"),
    path('signup/', signup, name="signup"),
    path('logout/', logout, name='logout'),
    path('add-todo/', add_todo, name='add-todo'),
    path('update-todo/<int:id>/<str:status>/', update_todo, name='update-todo'),
    path('delete-todo/<int:id>/', delete_todo, name='delete-todo')
]
