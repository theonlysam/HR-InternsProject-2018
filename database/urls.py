from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('database/home', views.home, name='home'),
    path('database/homex', views.homex, name='homex'),
    path('database/search', views.search, name='search'),    
    path('database/searchx', views.searchx, name='searchx'),
    path('database/view/<key>/', views.view, name='view'),    
    path('database/viewx/<keyx>/', views.viewx, name='viewx'),
    path('database/edit_record/<key>/', views.edit_record, name='edit_record'),
    path('database/edit_intern_history/<keyy>/<key>/', views.edit_intern_history, name='edit_intern_history'),
    path('database/edit_intern_qualification/<keyy>/<key>/', views.edit_intern_qualification, name='edit_intern_qualification'), 
    path('database/edit_recordx/<keyx>/', views.edit_recordx, name='edit_recordx'),
    path('database/edit_xemployee_history/<keyyx>/<keyx>/', views.edit_xemployee_history, name='edit_xemployee_history'),
    path('database/edit_xemployee_degrees/<keyyx>/<keyx>/', views.edit_xemployee_degrees, name='edit_xemployee_degrees'),
    path('database/update_record/<key>/', views.update_record, name='update_record'),     
    path('database/update_intern_history/<keyy>/<key>/', views.update_intern_history, name='update_intern_history'),
    path('database/update_intern_qualification/<keyy>/<key>/', views.update_intern_qualification, name='update_intern_qualification'), 
    path('database/update_recordx/<keyx>/', views.update_recordx, name='update_recordx'),
    path('database/update_xemployee_history/<keyyx>/<keyx>/', views.update_xemployee_history, name='update_xemployee_history'),
    path('database/update_xemployee_degrees/<keyyx>/<keyx>/', views.update_xemployee_degrees, name='update_xemployee_degrees'),
    path('database/new', views.new, name='new'),
    path('database/newx', views.newx, name='newx'),
    path('database/historyform',views.history, name='history'),
    path('database/qualificationform',views.qualification, name='qualification'),
    path('database/update_record/<key>/', views.update_record, name='update_record'),    
    path('database/new', views.new, name='new'),
    path('database/historyformx',views.historyx, name='historyx'),
    path('database/employee_degreex',views.employee_degreex, name='employee_degreex'),
]
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
