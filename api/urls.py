from django.urls import path

from . import views


urlpatterns = [
    path('', views.index),
    path('todos', views.todos),
    path('todos/<str:id>', views.todo),
    path('todos/<str:id>/complete', views.complete_todo),
]
