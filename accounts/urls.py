
from django.urls import path
from django.contrib.auth import views as auth_views

from accounts.views import UserTypeRedirectView, home, register, Greeting, login

urlpatterns = [
    path('logi', UserTypeRedirectView.as_view(), name='user_type'),
    path('', home, name="home"),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('greeting/<face_id>/', Greeting, name='greeting'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password/change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password/change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password/reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password/reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password/reset/confirm/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password/reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
