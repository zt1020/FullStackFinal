from django.urls import path
from django.conf.urls import url
#import internship.views
#from internship.views.import_alldata import *
from . import views

urlpatterns = [

        path('import_file/', views.import_file, name='import_file'),
        #path('import_internship/', views.import_internship, name='import internship')
    ]
