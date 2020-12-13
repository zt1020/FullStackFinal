"""
urls.py
Contributors: Snehitha, harshani
updated : 11/16/2020
"""
from django.urls import path
# from django.conf.urls import url
from internship.views import HomepageView,display_students,display_internship,register_page,updateStudent,remove_data
from internship.views import createStudent, updateInternship, createInternship
from internship.views import display_internshipassignment,deleteStudent,deleteInternship
from internship import views

urlpatterns = [
        path('home/', HomepageView.as_view(), name='home'),
        path('import_file/', views.import_file, name='import_file'),
        path('display_students/', display_students, name='display_students'),
        path('display_internship/', display_internship,
            name='display_internship'),
        path('display_internshipassignment/', display_internshipassignment,
            name='display_internshipassignment'),
        path('', register_page, name='register'),
        path('logout/', views.logout_request, name='logout'),
        path('login/', views.login_request, name='login'),
        path('update_student/<int:pk>/', views.updateStudent, name="update_student"),

        path('delete_student/<int:pk>/', views.deleteStudent, name="delete_student" ),

        path('create_student/', views.createStudent, name="create_student"),
        path('update_internship/<int:pk>/', views.updateInternship, name="update_internship"),

        path('delete_internship/<int:pk>/', views.deleteInternship, name="delete_internship" ),

        path('create_internship/', views.createInternship, name="create_internship"),
        path('remove_data/', remove_data, name='remove_data' ),

        path('update_internshipAssignment/<int:pk>/', views.updateInternshipAssignment, name="update_internshipAssignment"),

        path('delete_internshipassignment/<int:pk>/', views.deleteInternshipAssignment, name="delete_internshipassignment" ),

        path('create_internshipassignment/', views.createInternshipAssignment, name="create_internshipassignment" )
        # url(r'^user/create$', UserCreateView.as_view(), name='user_create'),
    ]
