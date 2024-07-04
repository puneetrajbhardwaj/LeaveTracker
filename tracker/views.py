from django.shortcuts import render
from django.http import JsonResponse
from .models import Tracker
from manager.models import Employee,Leave
from manager.manager_serializer import EmployeeSerializer
from django.db.models import Count,F,Q
import json
from datetime import datetime,timedelta
# from rest_framework.renderers import JSONRenderer
# from io import BytesIO
# from rest_framework.parsers import JSONParser
# from django.core import serializers


def AddTracker(request):
    employees=Employee.objects.all()
    leaves=Leave.objects.all()
    return render(request,'tracker/AddTracker.html',{'employees':employees,'leaves':leaves})

def CreateTracker(request):
    try:
        employee_uid=request.GET['employee_uid']
        employee_uid=employee_uid[employee_uid.index("(")+1:employee_uid.index(")")]
        employee=Employee.objects.get(employee_uid=employee_uid) 
        leave_name=request.GET['leave_name']
        leave=Leave.objects.get(leave_name=leave_name)
        start_date=str(request.GET['start_date'])
        start_date=datetime.strptime(start_date,'%Y-%m-%d').date()
        end_date=str(request.GET['end_date'])
        end_date=datetime.strptime(end_date,"%Y-%m-%d").date()
        date=start_date
        while(date<=end_date):
            Tracker.objects.create(employee=employee,leave=leave,date=date)
            date=date+timedelta(days=1)
        employees=Employee.objects.all()
        leaves=Leave.objects.all()    
        return render(request,'tracker/AddTracker.html',{'employees':employees,'leaves':leaves,'result':'Entry submitted successfully.'})
    except Exception as e:
        print(e,'-------------------------------------------------------------')
        return render(request,'tracker/AddTracker.html',{'employees':employees,'leaves':leaves,'result':'error'+e})


def ShowTracker(request):
    data=Tracker.objects.all().order_by("employee__employee_name","-date")
    leaves=Leave.objects.all()
    return render(request,'tracker/ShowTracker.html',{'data':data,'leaves':leaves})

def GetEmployeeJSON(request):
    employees=list(Employee.objects.values())
    return JsonResponse(employees,safe=False)

def GetGlanceJSON(request):
    # leave_counts = Tracker.objects.annotate(employee_uid=F('employee'),leave_count=Count('leave'),leave_name=F('leave')).values('employee_uid','leave_name','leave_count')
    # print(leave_counts,'---------------------------------------------')
    # leave_counts = Employee.objects.annotate(leave_count=Count('tracker__leave__leave_name')).values('employee_uid','leave_count')
    # print(leave_counts,'---------------------------------------------')
    # leave_counts = Tracker.objects.values('employee', 'employee__employee_name', 'leave', 'leave__leave_alias').annotate(count=Count('leave')).order_by('employee', 'leave')
    # print(leave_counts,'---------------------------------------------')
    leave_counts=[]
    employees=Employee.objects.all().order_by("employee_name")
    for employee in employees:
        leaves=Leave.objects.all()
        dict={}
        dict['employee_name']=str(employee)
        dict['employee_uid']=str(employee.employee_uid)
        for leave in leaves:
            leave_count=Tracker.objects.filter(Q(employee=employee) & Q(leave=leave)).values().count()
            dict[str(leave.leave_alias)]=int(leave_count)
        leave_counts.append(dict)   
    return JsonResponse(leave_counts,safe=False)

def TrackerGlance(request):
    leaves=Leave.objects.all()    
    return render(request,'tracker/TrackerGlance.html',{'leaves':leaves})

def FilterTracker(request):
    return render(request,'tracker/FilterTracker.html',{})    

def DisplayFilterResult(request):
    try:
        employee_uid=request.GET['filter_employee_uid']
        employee_uid=employee_uid[employee_uid.index("(")+1:employee_uid.index(")")]
        employee=Employee.objects.get(employee_uid=employee_uid) 
        start_date=request.GET['start_date']
        end_date=request.GET['end_date']
        data=Tracker.objects.filter(Q(employee=employee) & Q(date__gte=start_date) & Q(date__lte=end_date))
        print(data)
        leaves=Leave.objects.all()
        return render(request,'tracker/ShowTracker.html',{'data':data,'leaves':leaves})
    except Exception as e:
        print(e)
        return ShowTracker(request)

def SeeDetails(request,pk):
    data=Tracker.objects.filter(employee__employee_uid=pk)
    leaves=Leave.objects.all()
    return render(request,'tracker/ShowTracker.html',{'data':data,'leaves':leaves})

def EditEntry(request,pk):
    try:    
        data=Tracker.objects.get(tracker_id=pk)
        employee_uid=request.GET['employee_uid']
        employee_uid=employee_uid[employee_uid.index("(")+1:employee_uid.index("(")+7]
        employee=Employee.objects.get(employee_uid=employee_uid) 
        leave_name=request.GET['leave_name']
        leave=Leave.objects.get(leave_name=leave_name)
        date=request.GET['tracker_date']
        data.employee=employee
        data.leave=leave
        data.date=date
        data.save()
        return ShowTracker(request)
    except Exception as e:
        print(e,'----------------------------------------------------------------------')
        return ShowTracker(request)

def YearView(request,uid):
     return render(request,'tracker/YearView.html',{'uid':uid})   

def GetDateColorJSON(request,employee_uid,year):
    year=datetime.strptime(year,"%Y").year
    data=Tracker.objects.filter(Q(employee__employee_uid=employee_uid) & Q(date__year=year)).values('leave__leave_alias','leave__leave_color','date')
    for row in data:
        row['date']=row['date'].strftime("%Y-%m-%d")
    data=list(data)    
    return JsonResponse(data,safe=False)
    
def DeleteEntry(request,tracker_id):
    entry=Tracker.objects.get(tracker_id=tracker_id)
    entry.delete()    
    return ShowTracker(request)
    
# def CleanUp(request):
#     print("Hiiiiiiiiiiii")
#     Tracker.objects.all().delete()
#     return ShowTracker(request)




        





