# Generated by Django 4.2.2 on 2023-06-18 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_delete_myappactualite_delete_myappartisanat_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Admin',
        ),
        migrations.DeleteModel(
            name='AuthGroup',
        ),
        migrations.DeleteModel(
            name='AuthGroupPermissions',
        ),
        migrations.DeleteModel(
            name='AuthPermission',
        ),
        migrations.DeleteModel(
            name='AuthUser',
        ),
        migrations.DeleteModel(
            name='AuthUserGroups',
        ),
        migrations.DeleteModel(
            name='AuthUserUserPermissions',
        ),
        migrations.DeleteModel(
            name='DjangoAdminLog',
        ),
        migrations.DeleteModel(
            name='DjangoContentType',
        ),
        migrations.DeleteModel(
            name='DjangoMigrations',
        ),
        migrations.DeleteModel(
            name='DjangoSession',
        ),
        migrations.DeleteModel(
            name='Human',
        ),
        migrations.DeleteModel(
            name='MyappClient',
        ),
        migrations.DeleteModel(
            name='MyappHotel',
        ),
    ]
