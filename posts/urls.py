from django.urls import path

from .views import post_list, post_details

app_name = "posts"
urlpatterns = [
    path("posts/", post_list, name="list" ),
    path("posts/<id>/", post_details, name="details" ),

]