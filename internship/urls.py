"""
urls.py
Contributors: Snehitha, harshani
updated : 11/16/2020
"""
from django.urls import path
# from django.conf.urls import url
from internship.views import HomepageView,display_students,display_internship
from internship.views import display_internshipassignment
from internship import views
# from .views import ListView


urlpatterns = [
        path('', HomepageView.as_view(), name='home'),
        path('import_file/', views.import_file, name='import_file'),
        path('display_students/', display_students, name='display_students'),
        path('display_internship/', display_internship,
            name='display_internship'),
        path('display_internshipassignment/', display_internshipassignment,
            name='display_internshipassignment')
    ]
