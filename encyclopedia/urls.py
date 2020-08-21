from django.urls import path

from . import views

app_name = "encyclopedia"

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>", views.return_results, name="return_results"),
    path("create_page", views.add_entry, name="add_entry"),
    path("random", views.random_page, name="random_page")

]
