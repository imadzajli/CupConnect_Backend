# Generated by Django 4.2.2 on 2024-02-26 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dishe',
            name='d',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
