
from django.urls import path
from .import views

urlpatterns = [
    path('', views.Home, name="Home"),
    path('delete/<int:taskid>/',views.delete,name="delete"),
    path('update/<int:id>/', views.update, name="update"),
    path('cbvHome/',views.Tasklistview.as_view (),name="cbvHome"),
    path('cbvdetail/<int:pk>/', views.Taskdetailview.as_view(), name="cbvdetail"),
    path('cbvupdate/<int:pk>/', views.Taskupdateview.as_view(), name="cbvupdate"),
    path('cbvdelete/<int:pk>/', views.Taskdeleteview.as_view(), name="cbvdelete"),

]