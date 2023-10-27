from django.urls import path

from . import views

urlpatterns = [
    path("index", views.index, name="index"),
    path("index", views.index_cat, name="index_cat"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create, name="new"),
    path("listing/<int:id>", views.list, name="list"),
    path("bid/<int:id>", views.current, name="bid"),
    path("mypage", views.mypage, name="mypage"),
    path("edit/<int:id>", views.edit, name="edit"),
    path("del/<int:id>", views.delete, name="del"),
    path("wishadd/<int:id>", views.add, name="add"),
    path("wishremove/<int:id>", views.remove, name="remove"),
    path("watchlist", views.watch, name="watch"),
    path("comments/<int:id>", views.comm, name="com"),
    path("sell/<int:id>", views.sell, name="sell"),
    path("solditems", views.solditems, name="solditems"),
    path("removebid/<int:id>", views.removebid, name="removebid"),
]
