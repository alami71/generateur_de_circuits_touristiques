from django.urls import path
from . import views

app_name = "myapp"

urlpatterns = [
    path("", views.accueil, name="accueil"),
    path("home/", views.accueil, name="home"),
    path("circuit/", views.circuit, name="circuit"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("services/", views.services, name="services"),
    path("genere_ciruit/", views.genere_ciruit, name="genere_ciruit"),
    path("test/", views.test, name="test"),
    path(
        "destination/<int:destination_id>/",
        views.destination_page,
        name="destination_page",
    ),
    path("genere_un_circuit", views.genere_un_circuit, name="genere_un_circuit"),
    path("search_cities", views.search_cities, name="search_cities"),
    path("search_cities_tcircuit", views.Tcircuit, name="Tcircuit"),
    path("hotel_page/<int:hotel_id>/", views.hotel_page, name="hotel_page"),
    path("restaurant_page/<int:Restaurant_id>/", views.restaurant_page, name="restaurant_page"),
    path("ville_page/<int:id_ville>/", views.ville_page, name="ville_page"),
    
]
