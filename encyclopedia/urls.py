from django.urls import path

from . import views

app_name = "encyclopedia"

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>/", views.return_results, name="return_results"),
    path("encyclopedia/create_page", views.create_page, name="create_page"),
    path("encyclopedia/random", views.random_page, name="random_page")

]
