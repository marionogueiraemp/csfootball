# Generated by Django 5.1.3 on 2024-11-27 22:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("competitions", "0003_competitionstandings_competition_end_date_and_more"),
        ("teams", "0004_alter_team_owner"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name="playerapplication",
            name="created_at",
        ),
        migrations.RemoveField(
            model_name="team",
            name="players",
        ),
        migrations.RemoveField(
            model_name="transferrequest",
            name="created_at",
        ),
        migrations.AlterField(
            model_name="playerapplication",
            name="player",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="applications",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="playerapplication",
            name="status",
            field=models.CharField(
                choices=[
                    ("Pending", "Pending"),
                    ("Accepted", "Accepted"),
                    ("Rejected", "Rejected"),
                ],
                default="Pending",
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="team",
            name="competitions",
            field=models.ManyToManyField(
                related_name="teams", to="competitions.competition"
            ),
        ),
        migrations.AlterField(
            model_name="team",
            name="name",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="team",
            name="owner",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="owned_teams",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="transferrequest",
            name="status",
            field=models.CharField(
                choices=[
                    ("Pending", "Pending"),
                    ("Approved", "Approved"),
                    ("Rejected", "Rejected"),
                ],
                default="Pending",
                max_length=20,
            ),
        ),
        migrations.CreateModel(
            name="Player",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                (
                    "team",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="players",
                        to="teams.team",
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="transferrequest",
            name="player",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="transfer_requests",
                to="teams.player",
            ),
        ),
    ]
