from django.urls import path
from . import views

urlpatterns = [
 path("index", views.index, name="index"),
 path("desc", views.desc, name="desc"),
 path("newmentor", views.newmentor, name="newmentor"),
 path("newstudent", views.newstudent, name="newstudent"),
 path("displaystudent", views.displaystudent, name="displaystudent"),
 path("update/<str:stuid>", views.update, name="update"),
 path("update/updatestudent/<str:stuid>", views.updatestudent, name="updatestudent"),
 path("delete/<str:stuid>", views.delete, name="delete"),
 path("delete/deletestudent/<str:stuid>", views.deletestudent, name="deletestudent")


 ]
