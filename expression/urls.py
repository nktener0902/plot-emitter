from django.urls import path

from . import views

app_name = "expression"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("history/", views.HistoryView.as_view(), name="history"),
]
