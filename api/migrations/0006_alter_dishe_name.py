# Generated by Django 4.2.2 on 2024-02-26 21:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0005_alter_place_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dishe",
            name="name",
            field=models.CharField(max_length=50),
        ),
    ]
