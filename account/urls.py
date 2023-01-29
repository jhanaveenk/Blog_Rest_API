from django.contrib import admin
from django.urls import path
from account.views import register_view, LoginView

urlpatterns = [
    path('register/', register_view.as_view()),
    path('login/', LoginView.as_view()),

]