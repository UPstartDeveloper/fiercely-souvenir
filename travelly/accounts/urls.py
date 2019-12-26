from django.urls import path
from django.contrib.auth import views as auth_views
from accounts.views import (
    launch_page,
    SignUpView,
    ProfileDetail,
    AccountUpdate,
    UserDelete,
    BeginPasswordChange,
    PasswordResetView,
    PasswordResetConfirm,
)

app_name = 'accounts'
urlpatterns = [
    # Launch page
    path('', launch_page, name="launch"),
    # Base auth: signup, logim, and logout views
    path('signup/', SignUpView.as_view(), name='new-user'),
    path('login/',
         auth_views.LoginView.as_view(template_name="accounts/login.html"),
         name='login'),
    path('logout/',
         auth_views.LogoutView.as_view(), name='logout'),
    # Advanced auth: change password, reset password
    path('password-change/', BeginPasswordChange.as_view(),
         name='start_passwd_change'),
    path('password-change/done/',
         auth_views.PasswordChangeDoneView.as_view(template_name=(
            'accounts/password/change-complete.html')),
         name='passwd_change_complete'),
    path('reset-password/', PasswordResetView.as_view(),
         name='passwd_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
          template_name='accounts/password/reset/email_sent.html'),
         name='password_reset_email_sent'),
    path('password-reset-confirm/<uidb64>/<token>/',
         PasswordResetConfirm.as_view(), name='passwd_reset_confirm'),
    # PasswordResetComplete view
    # profile READ, UPDATE, and DELETE
    path('<int:pk>/profile/', ProfileDetail.as_view(), name='acct_info'),
    path('<int:pk>/change-account-details/', AccountUpdate.as_view(),
         name='change-info'),
    path('<int:pk>/delete-account/', UserDelete.as_view(),
         name='delete_account'),
]
