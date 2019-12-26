from django.urls import path
from django.contrib.auth import views as auth_views
from accounts.views import (
    launch_page,
    SignUpView,
    ProfileDetail,
    AccountUpdate,
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
    # profile READ, UPDATE, and DELETE
    path('<int:pk>/profile/', ProfileDetail.as_view(), name='acct_info'),
    path('<int:pk>/change-account-details/', AccountUpdate.as_view(),
         name='change-info'),
    # Advanced auth: reset password, change password?
]
