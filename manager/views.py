from django.shortcuts import render
from .models import Employee,Leave
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from math import ceil 
# Create your views here.

#Employee Management

def AddEmployee(request):
    return render(request,'manager/AddEmployee.html',{'result':''})

def ShowEmployees(request):
    employees=Employee.objects.all()
    params={'employees':employees}
    return render(request,'manager/ShowEmployees.html',params)

def CreateEmployee(request):
    try:
        employee_name=request.GET['employee_name']
        employee_uid=request.GET['employee_uid']
        Employee.objects.create(employee_uid=employee_uid,employee_name=employee_name) 
        return render(request,'manager/AddEmployee.html',{'result':'Employee Submitted Successfully.'})  
    except Exception as e:
        print(e)
        return render(request,'manager/AddEmployee.html',{'result':'error:'+e})

def EditEmployee(request,pk):
    employee=Employee.objects.get(employee_uid=pk)
    return render(request,'manager/EditEmployee.html',{'employee':employee})

def SaveEmployee(request,pk):
    try:
        employee=Employee.objects.get(employee_uid=pk)   
        employee_uid=request.GET['employee_uid']
        employee_name=request.GET['employee_name']
        if(pk!=employee_uid):
            employee.delete()
            Employee.objects.create(employee_uid=employee_uid,employee_name=employee_name)
        else:
            employee.employee_name=employee_name
            employee.save()
        return ShowEmployees(request)
    except Exception as e:
        print(e)
        return ShowEmployees(request)

    

def DeleteEmployee(request,pk):
    try:
        employee=Employee.objects.get(employee_uid=pk)
        employee.delete()
        return ShowEmployees(request)
    except Exception as e:
        print(e)
        return ShowEmployees(request)    


#Leaves 

def AddLeave(request):
    return render(request,'manager/AddLeave.html',{})

def CreateLeave(request):
    try:
        leave_name=request.GET['leave_name']
        leave_alias=request.GET['leave_alias']
        leave_color=request.GET['leave_color']
        Leave.objects.create(leave_name=leave_name,leave_alias=leave_alias,leave_color=leave_color) 
        return render(request,'manager/AddLeave.html',{"result":'Leave Submitted successfuly'})
    except Exception as e:
        return render(request,'manager/AddLeave.html',{"result":'error:'+e})


def ShowLeaves(request):
    leaves=Leave.objects.all()
    params={'leaves':leaves}
    return render(request,'manager/ShowLeaves.html',params)

def EditLeave(request,pk):
    leave=Leave.objects.get(leave_name=pk)
    return render(request,'manager/EditLeave.html',{'leave':leave})

def SaveLeave(request,pk):
    try:
        leave=Leave.objects.get(leave_name=pk)   
        leave_name=request.GET['leave_name']
        leave_alias=request.GET['leave_alias']
        leave_color=request.GET['leave_color']
        leave.leave_name=leave_name
        leave.leave_alias=leave_alias
        leave.leave_color=leave_color
        leave.save()
        return ShowLeaves(request)
    except Exception as e:
        print(e)
        return ShowLeaves(request)    
        
def DeleteLeave(request,pk):
    try:
        leave=Leave.objects.get(leave_name=pk)
        leave.delete()
        return ShowLeaves(request)
    except Exception as e:
        print(e)
        return ShowLeaves(request)    

