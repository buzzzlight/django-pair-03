from django.urls import path
from . import views

app_name = "letters"

urlpatterns = [
    path("", views.index, name="index"),
    path("email_send/", views.email_send, name="email_send"),
    path("<int:pk>/", views.email_detail, name="email_detail"),
]
