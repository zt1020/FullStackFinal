"""
urls.py
Contributors: Snehitha, harshani
updated : 11/16/2020
"""
from django.urls import path
# from django.conf.urls import url
from internship.views import HomepageView,display_students
from internship import views
from .views import ListView


urlpatterns = [
        path('', HomepageView.as_view(), name='home'),
        path('import_file/', views.import_file, name='import_file'),
        path('display_students/', display_students, name='display_students'),
        #path('import_internship/', views.import_internship, name='import internship')
    ]
