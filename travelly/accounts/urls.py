from django.urls import path
from django.contrib.auth import views as auth_views
from accounts.views import (
    launch_page,
    SignUpView,
)

app_name = 'accounts'
urlpatterns = [
    path('', launch_page, name="launch"),
    path('signup/', SignUpView.as_view(), name='new-user'),
    path('login/',
         auth_views.LoginView.as_view(template_name="accounts/login.html"),
         name='login'),
    path('logout/',
         auth_views.LogoutView.as_view(), name='logout'),
]
