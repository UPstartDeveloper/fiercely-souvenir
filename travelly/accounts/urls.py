from django.urls import path
from accounts.views import launch_page

app_name = 'accounts'
urlpatterns = [
    path('', launch_page, name="launch"),
]
