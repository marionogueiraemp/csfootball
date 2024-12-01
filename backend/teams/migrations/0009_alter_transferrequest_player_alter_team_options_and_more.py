# Generated by Django 5.1.3 on 2024-11-30 13:15

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("teams", "0008_alter_player_user"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="transferrequest",
            name="player",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="transfers",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterModelOptions(
            name="team",
            options={"ordering": ["-points", "-goals_scored"]},
        ),
        migrations.RemoveField(
            model_name="team",
            name="competitions",
        ),
        migrations.AddField(
            model_name="playerapplication",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="team",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="team",
            name="description",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="team",
            name="draws",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="team",
            name="goals_conceded",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="team",
            name="goals_scored",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="team",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="team",
            name="is_verified",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="team",
            name="losses",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="team",
            name="matches_played",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="team",
            name="players",
            field=models.ManyToManyField(
                related_name="teams", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="team",
            name="points",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="team",
            name="wins",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="transferrequest",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="playerapplication",
            name="status",
            field=models.CharField(
                choices=[
                    ("PENDING", "Pending"),
                    ("ACCEPTED", "Accepted"),
                    ("REJECTED", "Rejected"),
                ],
                default="PENDING",
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="team",
            name="name",
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name="team",
            name="owner",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="owned_team",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="transferrequest",
            name="from_team",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="transfers_out",
                to="teams.team",
            ),
        ),
        migrations.AlterField(
            model_name="transferrequest",
            name="status",
            field=models.CharField(
                choices=[
                    ("PENDING", "Pending"),
                    ("ACCEPTED", "Accepted"),
                    ("REJECTED", "Rejected"),
                ],
                default="PENDING",
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="transferrequest",
            name="to_team",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="transfers_in",
                to="teams.team",
            ),
        ),
        migrations.DeleteModel(
            name="Player",
        ),
    ]