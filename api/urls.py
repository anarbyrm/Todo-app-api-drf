from django.urls import path
from .views import (
    links,
    task_list,
    task_detail,
    task_create, 
    task_update,
    task_delete
)


urlpatterns = [
    path('', links),
    path('task-list/', task_list),
    path('task-detail/<int:pk>/', task_detail),
    path('task-create/', task_create),
    path('task-update/<int:pk>/', task_update),
    path('task-delete/<int:pk>/', task_delete),

]