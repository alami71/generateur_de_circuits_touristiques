# Generated by Django 4.2.2 on 2023-06-15 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_authgroup_authgrouppermissions_authpermission_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MyappActualite',
        ),
        migrations.DeleteModel(
            name='MyappArtisanat',
        ),
        migrations.DeleteModel(
            name='MyappChambre',
        ),
        migrations.DeleteModel(
            name='MyappCircuitvoyage',
        ),
        migrations.DeleteModel(
            name='MyappDestination',
        ),
        migrations.DeleteModel(
            name='MyappMateriels',
        ),
        migrations.DeleteModel(
            name='MyappMessages',
        ),
        migrations.DeleteModel(
            name='MyappMoussem',
        ),
        migrations.DeleteModel(
            name='MyappPlat',
        ),
        migrations.DeleteModel(
            name='MyappReservation',
        ),
        migrations.DeleteModel(
            name='MyappRestaurant',
        ),
    ]
