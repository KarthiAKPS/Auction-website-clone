from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create, name="new"),
    path("listing/<str:t>", views.list, name="list"),
    path("listing/<str:name>/<int:price>", views.current, name="current")
]
