from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_page, name='todo_page'),
    path('details', views.details, name='details'),
    path('delete/<int:taskid>/', views.deletetask, name='deletetask'),
    path('edit/<int:id>/', views.updatetask, name='updatetask'),
    path('cbvhome/',views.Tasklistview.as_view(),name='cbvhome'),
    path('cbvdetail/<int:pk>/',views.TaskDetailView.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>/',views.TaskUpdateView.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.TaskDeleteView.as_view(),name='cbvdelete')
]
