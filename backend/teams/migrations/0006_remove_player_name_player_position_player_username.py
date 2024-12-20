# Generated by Django 5.1.3 on 2024-11-27 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("teams", "0005_remove_playerapplication_created_at_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="player",
            name="name",
        ),
        migrations.AddField(
            model_name="player",
            name="position",
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="player",
            name="username",
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
    ]
