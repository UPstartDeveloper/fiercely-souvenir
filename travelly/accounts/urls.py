from django.urls import path
from accounts.views import (
    launch_page,
    SignUpView,
)

app_name = 'accounts'
urlpatterns = [
    path('', launch_page, name="launch"),
    path('signup/', SignUpView.as_view(), name='new-user'),
]
