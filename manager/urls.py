from django.urls import path
from . import views

urlpatterns=[
    #Employee
    path('addemployee/',views.AddEmployee),
    path('showemployees/',views.ShowEmployees),
    path('createemployee/',views.CreateEmployee),
    path('editemployee/<str:pk>',views.EditEmployee),
    path('saveemployee/<str:pk>',views.SaveEmployee),
    path('deleteemployee/<str:pk>',views.DeleteEmployee),

    #Leave
    path('addleave/',views.AddLeave),
    path('createleave/',views.CreateLeave),
    path('showleaves/',views.ShowLeaves),
    path('editleave/<str:pk>',views.EditLeave),
    path('saveleave/<str:pk>',views.SaveLeave),
    path('deleteleave/<str:pk>',views.DeleteLeave),
    
]