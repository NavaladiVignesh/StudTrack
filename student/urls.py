from django.urls import path, include
from student import views

urlpatterns = [
    path('std',views.std,name="std"),
    path('list',views.read_data,name='list'),
    path('delete/<int:id>',views.destroy,name="delete"),
    path('edt/<int:id>',views.edit,name="edt"),
]