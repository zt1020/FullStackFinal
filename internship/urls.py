"""
urls.py
Contributors: Snehitha, harshani
updated : 11/16/2020
"""
from django.urls import path
# from django.conf.urls import url
from internship.views import HomepageView
from internship import views


urlpatterns = [
        path('', HomepageView.as_view(), name='home'),
        path('import_file/', views.import_file, name='import_file'),
        #path('import_internship/', views.import_internship, name='import internship')
    ]
