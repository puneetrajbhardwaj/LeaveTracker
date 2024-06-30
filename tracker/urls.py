from django.urls import path
from . import views

urlpatterns=[
    path('showtracker/',views.ShowTracker),
    path('addtracker/',views.AddTracker),
    path('createtracker/',views.CreateTracker),
    path('getemployeejson/',views.GetEmployeeJSON),
    path('trackerglance/',views.TrackerGlance),
    path('getglancejson/',views.GetGlanceJSON),
    path('filtertracker/',views.FilterTracker),
    path('displayfilterresult/',views.DisplayFilterResult),
    path('seedetails/<str:pk>',views.SeeDetails),
    path('editentry/<int:pk>',views.EditEntry),
    path('deleteentry/<int:tracker_id>',views.DeleteEntry),
    path('yearview/<str:uid>',views.YearView),
    path('getdatecolorjson/<str:employee_uid>/<str:year>',views.GetDateColorJSON),
    # path('cleanup/',views.CleanUp),
]