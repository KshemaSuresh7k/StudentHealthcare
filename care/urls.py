from django.urls import path
from . import views

urlpatterns =[

    path('',views.index,name='index'),
    path('tlogin/',views.tlogin,name='tlogin'),
    path('tlog/',views.tlog,name='tlog'),
    path('thome/',views.thome,name='thome'),
    path('addstudents/',views.addstudents,name='addstudents'),
    path('slogin/',views.slogin,name='slogin'),
    path('slog/',views.slog,name='slog'),
    path('shome/',views.shome,name='shome'),
    path('viewstudent/',views.viewstudent,name='viewstudent'),
    path('healthcare/',views.healthcare,name='healthcare'),
    path('viewhealth/',views.viewhealth,name='viewhealth'),
    path('viewfile/<str:pk>',views.viewfile,name='viewfile'),
    path('addvaccination/',views.addvaccination,name='addvaccination'),
    path('addfile/',views.addfile,name='addfile'),
    path('tviewhealth/',views.tviewhealth,name='tviewhealth'),

]

