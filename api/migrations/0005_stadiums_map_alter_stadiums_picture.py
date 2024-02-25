# Generated by Django 4.2.2 on 2024-02-25 09:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0004_rename_counrty_stadiums_country"),
    ]

    operations = [
        migrations.AddField(
            model_name="stadiums",
            name="map",
            field=models.CharField(default="hh", max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="stadiums",
            name="picture",
            field=models.CharField(max_length=500),
        ),
    ]
