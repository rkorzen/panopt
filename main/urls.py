from django.urls import path
from .views import register_request, homepage
app_name = "main"

urlpatterns = [
    path("", homepage, name="homepage"),                 # /
    path("register/", register_request, name='register') # /register/
]