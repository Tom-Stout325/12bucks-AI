from django.urls import path, include, reverse_lazy
from django.contrib.auth import views as auth_views
from .views import *



urlpatterns = [
    # Custom User Views
    path('', login_view, name="my-login"), 
    path('register/', register, name="register"),
    path('login/', login_view, name="my-login"), 
    path('logout/', logoutView, name="logout"),

    # Password Reset Views
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='app/password_reset.html',email_template_name='app/password_reset_email.html', success_url=reverse_lazy('app/password_reset_done')), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html', success_url=reverse_lazy('app/password_reset_complete')), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'), name='password_reset_complete'),

    # Password Change Views
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='app/password_change.html', success_url=reverse_lazy('app/password_change_done')), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view( template_name='app/password_change_done.html'), name='password_change_done'),
]