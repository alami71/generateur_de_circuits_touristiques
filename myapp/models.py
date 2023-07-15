# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Actualite(models.Model):
    id_actu = models.AutoField(primary_key=True)
    id_circuit = models.ForeignKey(
        "CircuitVoyage", models.DO_NOTHING, db_column="id_circuit"
    )
    titre_actu = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = "actualite"

    def __str__(self):
        return self.titre_actu


class Artisanat(models.Model):
    id_artisanat = models.AutoField(primary_key=True)
    nom_artisanat = models.CharField(max_length=40)
    image_artisanat = models.CharField(max_length=255)
    date_modification = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "artisanat"

    def __str__(self):
        return self.nom_artisanat


class Chambre(models.Model):
    num_chambre = models.AutoField(primary_key=True)
    id_hotel = models.ForeignKey("Hotel", models.DO_NOTHING, db_column="id_hotel")
    type_chambre = models.CharField(max_length=20)
    prix_chambre = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = "chambre"
        unique_together = (("num_chambre", "id_hotel"),)

    def __str__(self):
        return f"Chambre {self.num_chambre}"


class CircuitVoyage(models.Model):
    id_circuit = models.AutoField(primary_key=True)
    ville_depart = models.CharField(max_length=30)
    ville_arrivee = models.CharField(max_length=30)
    trajet = models.TextField()
    date_depart = models.DateTimeField()
    duree = models.IntegerField()
    image_cover = models.CharField(max_length=255)
    image_trajet = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    fin_reservation = models.DateField()

    class Meta:
        managed = False
        db_table = "circuit_voyage"

    def __str__(self):
        return f"Circuit {self.id_circuit}"


# Add the remaining classes with their __str__() methods


class Client(models.Model):
    id_client = models.AutoField(primary_key=True)
    nom_client = models.CharField(max_length=30)
    prenom_client = models.CharField(max_length=30)
    email_client = models.CharField(max_length=60)
    login_client = models.CharField(max_length=40)
    password_client = models.CharField(max_length=40)
    date_inscription = models.DateTimeField()
    code = models.IntegerField()
    status = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = "client"

    def __str__(self):
        return f"{self.prenom_client} {self.nom_client}"


class Hotel(models.Model):
    id_hotel = models.AutoField(primary_key=True)
    nom_hot = models.CharField(max_length=30)
    ville_hot = models.CharField(max_length=20)
    province = models.CharField(max_length=30)
    image_hot1 = models.CharField(max_length=255)
    image_hot2 = models.CharField(max_length=255)
    image_hot3 = models.CharField(max_length=255)
    localisation_hot = models.CharField(max_length=255)
    carte_hot = models.TextField()
    nbchambres = models.IntegerField(
        db_column="nbChambres"
    )  # Field name made lowercase.
    classe_hot = models.IntegerField()
    date_modification = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "hotel"

    def __str__(self):
        return self.nom_hot


# Add the remaining classes with their __str__() methods


class Materiels(models.Model):
    id_materiel = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=40)
    image1 = models.CharField(max_length=255)
    image2 = models.CharField(max_length=255)
    image3 = models.CharField(max_length=255)
    prix = models.DecimalField(max_digits=10, decimal_places=0)
    description = models.TextField()

    class Meta:
        managed = False
        db_table = "materiels"

    def __str__(self):
        return self.nom


class Messages(models.Model):
    id_msg = models.AutoField(primary_key=True)
    date = models.DateTimeField()
    nom_redacteur = models.CharField(max_length=40)
    email_redacteur = models.CharField(max_length=60)
    sujet = models.CharField(max_length=60)
    message = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = "messages"

    def __str__(self):
        return self.sujet


class Moussem(models.Model):
    id_moussem = models.AutoField(primary_key=True)
    nom_moussem = models.CharField(max_length=30)
    ville_moussem = models.CharField(max_length=20)
    image_moussem1 = models.CharField(max_length=255)
    image_moussem2 = models.CharField(max_length=255)
    image_moussem3 = models.CharField(max_length=255)
    description_moussem = models.TextField()
    date_modification = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "moussem"

    def __str__(self):
        return self.nom_moussem


class Plat(models.Model):
    id_plat = models.AutoField(primary_key=True)
    nom_plat = models.CharField(max_length=30)
    image_plat1 = models.CharField(max_length=255)
    image_plat2 = models.CharField(max_length=255)
    image_plat3 = models.CharField(max_length=255)
    description_plat = models.TextField()
    date_modification = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "plat"

    def __str__(self):
        return self.nom_plat


class Reservation(models.Model):
    id_res = models.AutoField(primary_key=True)
    id_client = models.ForeignKey(Client, models.DO_NOTHING, db_column="id_client")
    id_hotel = models.ForeignKey(Hotel, models.DO_NOTHING, db_column="id_hotel")
    tel_client = models.IntegerField()
    type_chambre = models.CharField(max_length=25)
    nb_personnes = models.IntegerField(blank=True, null=True)
    date_debut = models.DateField()
    date_fin = models.DateField()
    prix = models.DecimalField(max_digits=10, decimal_places=0)
    type_paiement = models.CharField(max_length=30)
    date_res = models.DateTimeField()
    status = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = "reservation"

    def __str__(self):
        return f"Reservation {self.id_res}"


class ReservationMateriel(models.Model):
    id_res = models.AutoField(primary_key=True)
    id_client = models.IntegerField()
    id_materiel = models.IntegerField()
    tel_client = models.IntegerField()
    nb_personnes = models.IntegerField()
    date_debut = models.DateField()
    date_fin = models.DateField()
    prix = models.DecimalField(max_digits=10, decimal_places=0)
    type_paiement = models.CharField(max_length=40)
    status = models.CharField(max_length=30)
    date_res = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "reservation_materiel"

    def __str__(self):
        return f"ReservationMateriel {self.id_res}"


class ReservationVoyage(models.Model):
    id_reservation = models.AutoField(primary_key=True)
    id_client = models.ForeignKey(Client, models.DO_NOTHING, db_column="id_client")
    id_circuit = models.ForeignKey(
        CircuitVoyage, models.DO_NOTHING, db_column="id_circuit"
    )
    tel_client = models.IntegerField()
    nb_personnes = models.IntegerField()
    prix = models.DecimalField(max_digits=10, decimal_places=0)
    type_paiement = models.CharField(max_length=60)
    date_res = models.DateTimeField()
    status = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = "reservation_voyage"

    def __str__(self):
        return f"ReservationVoyage {self.id_reservation}"


class Restaurant(models.Model):
    id_rest = models.AutoField(primary_key=True)
    nom_rest = models.CharField(max_length=30)
    ville_rest = models.CharField(max_length=30)
    province = models.CharField(max_length=20)
    image_rest1 = models.CharField(max_length=255)
    image_rest2 = models.CharField(max_length=255)
    image_rest3 = models.CharField(max_length=255)
    localisation_rest = models.CharField(max_length=255)
    carte_rest = models.TextField()
    description_rest = models.TextField()
    date_modification = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "restaurant"

    def __str__(self):
        return self.nom_rest


class Ville(models.Model):
    ville_id = models.BigAutoField(primary_key=True)
    ville_name = models.CharField(max_length=255)
    population = models.IntegerField(blank=True, null=True)
    area_km2 = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    country = models.CharField(max_length=255, blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, blank=True, null=True
    )
    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, blank=True, null=True
    )
    image1 = models.CharField(max_length=255, blank=True, null=True)
    image2 = models.CharField(max_length=255, blank=True, null=True)
    image3 = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ville"

    def __str__(self):
        return self.ville_name


class Destination(models.Model):
    id_dest = models.AutoField(primary_key=True)
    nom_dest = models.CharField(max_length=30)
    ville_dest = models.CharField(max_length=20)
    province = models.CharField(max_length=30)
    image_dest1 = models.CharField(max_length=255)
    image_dest2 = models.CharField(max_length=255)
    image_dest3 = models.CharField(max_length=255)
    localisation_dest = models.CharField(max_length=255)
    carte_dest = models.TextField()
    description_dest = models.TextField()
    date_modification = models.DateTimeField()
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    CATEGORY_CHOICES = (
        ("moussem", "Moussem"),
        ("endroit_naturel", "Endroit Naturel"),
        ("ksar", "Ksar"),
        ("souk", "Souk"),
    )
    categorie = models.CharField(max_length=50, choices=CATEGORY_CHOICES)

    class Meta:
        managed = False
        db_table = "destination"

    def __str__(self):
        return self.nom_dest
