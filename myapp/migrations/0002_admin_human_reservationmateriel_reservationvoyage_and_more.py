# Generated by Django 4.2.1 on 2023-05-22 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id_admin', models.AutoField(primary_key=True, serialize=False)),
                ('date_ajout', models.DateTimeField()),
                ('nom_admin', models.CharField(max_length=30)),
                ('prenom_admin', models.CharField(max_length=30)),
                ('email_admin', models.CharField(max_length=60)),
                ('login_admin', models.CharField(max_length=40)),
                ('password_admin', models.CharField(max_length=40)),
                ('photo_admin', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'admin',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Human',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=10, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'human',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ReservationMateriel',
            fields=[
                ('id_res', models.AutoField(primary_key=True, serialize=False)),
                ('id_client', models.IntegerField()),
                ('id_materiel', models.IntegerField()),
                ('tel_client', models.IntegerField()),
                ('nb_personnes', models.IntegerField()),
                ('date_debut', models.DateField()),
                ('date_fin', models.DateField()),
                ('prix', models.DecimalField(decimal_places=0, max_digits=10)),
                ('type_paiement', models.CharField(max_length=40)),
                ('status', models.CharField(max_length=30)),
                ('date_res', models.DateTimeField()),
            ],
            options={
                'db_table': 'reservation_materiel',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ReservationVoyage',
            fields=[
                ('id_reservation', models.AutoField(primary_key=True, serialize=False)),
                ('tel_client', models.IntegerField()),
                ('nb_personnes', models.IntegerField()),
                ('prix', models.DecimalField(decimal_places=0, max_digits=10)),
                ('type_paiement', models.CharField(max_length=60)),
                ('date_res', models.DateTimeField()),
                ('status', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'reservation_voyage',
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='actualite',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='artisanat',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='chambre',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='circuitvoyage',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='client',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='destination',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='hotel',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='materiels',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='messages',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='moussem',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='plat',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='reservation',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='restaurant',
            options={'managed': False},
        ),
    ]
