from django.urls import path

from . import views


# Register your urls here

urlpatterns = [path("", views.simple_view)]

# To register this URLS
# path("belaz_app/", include("apps.belaz_app.web.urls"))
