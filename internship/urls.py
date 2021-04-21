"""
urls.py
Contributors: Purnya, Zachary
updated : 04/011/2021
"""
from django.urls import path
from django.contrib.auth import views as auth_views
from internship import views
from internship.views import HomepageView

urlpatterns = [
        path('',  views.login_request, name='login'),
        path('home/', HomepageView.as_view(), name='home'),
        path('import_file/', views.import_file, name='import_file'),
        path('display_students/', views.display_students, name='display_students'),
        path('display_internship/', views.display_internship,
            name='display_internship'),
        path('display_internshipassignment/', views.display_internshipassignment,
            name='display_internshipassignment'),
        path('register/', views.register_page, name='register'),
        path('logout/', views.logout_request, name='logout'),
        path('login/', views.login_request, name='login'),
        path('update_student/<int:pk>/', views.update_student, name="update_student"),

        path('delete_student/<int:pk>/', views.delete_student, name="delete_student" ),

        path('create_student/', views.create_student, name="create_student"),
        path('update_internship/<int:pk>/', views.update_internship, name="update_internship"),

        path('delete_internship/<int:pk>/', views.delete_internship, name="delete_internship" ),

        path('create_internship/', views.create_internship, name="create_internship"),
        path('remove_data/', views.remove_data, name='remove_data' ),

        path('update_internshipAssignment/<int:pk>/',
            views.update_internshipassignment,
            name="update_internshipAssignment"),

        path('delete_internshipassignment/<int:pk>/',
            views.delete_internshipassignment,
            name="delete_internshipassignment" ),

        path('create_internshipassignment/',
            views.create_internshipassignment,
            name="create_internshipassignment" ),
        # url(r'^user/create$', UserCreateView.as_view(), name='user_create'),
        path('reset_password/', auth_views.PasswordResetView.as_view(template_name="reset_password.html"),
            name='reset_password'),
        path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"),
            name='password_reset_done'),
        path('reset/<uidb64>/<token>',
            auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"),
            name='password_reset_confirm'),
        path('reset_password_complete/',
            auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"),
            name='password_reset_complete')
    ]
