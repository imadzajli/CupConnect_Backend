# Generated by Django 5.0.2 on 2024-02-27 16:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0008_alter_user_gender"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="country",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="user",
            name="first_name",
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name="user",
            name="gender",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="user",
            name="last_name",
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name="user",
            name="phone",
            field=models.CharField(max_length=50),
        ),
    ]
