from django.urls import path

from . import views

app_name = "encyclopedia"

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>", views.return_results, name="return_results"),
    # path("search", views.search, name="search")

]
