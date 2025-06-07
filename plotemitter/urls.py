from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("accounts/", include("accounts.urls")),
    path("expression/", include("expression.urls")),
    path("admin/", admin.site.urls),
]
