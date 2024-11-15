# Generated by Django 5.1.3 on 2024-11-15 18:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("teams", "0003_remove_team_created_at_alter_team_name_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="team",
            name="owner",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="owned_team",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]