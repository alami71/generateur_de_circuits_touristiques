# Generated by Django 4.2.1 on 2023-05-23 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_actualite_table_alter_artisanat_table_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Human',
        ),
    ]