from django.contrib import admin
from django.urls import path
from .views import Index, Signup_view, Dashboard, Add_item, Edit_item, Delete_item
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("dashboard/", Dashboard.as_view(), name="dashboard"),
    path("add-item/", Add_item.as_view(), name="add-item"),
    path("edit-item/<int:pk>", Edit_item.as_view(), name="edit-item"),
    path("delete-item/<int:pk>", Delete_item.as_view(), name="delete-item"),
    path("signup/", Signup_view.as_view(), name="signup"),
    path("login/", auth_views.LoginView.as_view(template_name = "main_inventory/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name = "main_inventory/logout.html"), name="logout"),
]