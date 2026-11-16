from django.urls import path

from diligencias import views

app_name = "diligencias"

urlpatterns = [
    path("", views.DiligenciaListView.as_view(),name="lista"),
]