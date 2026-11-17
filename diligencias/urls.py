from django.urls import path

from diligencias import views

app_name = "diligencias"

urlpatterns = [
    path("", views.DiligenciaListView.as_view(),name="lista"),
    path("nova/", views.DiligenciaCreateView.as_view(), name="nova"),
    path("<int:pk>/editar/", views.DiligenciaUpdateView.as_view(), name="editar"),
]