# Generated by Django 4.2.2 on 2024-02-26 16:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0004_remove_place_distance_from_stadium"),
    ]

    operations = [
        migrations.AlterField(
            model_name="place",
            name="name",
            field=models.CharField(max_length=50),
        ),
    ]
