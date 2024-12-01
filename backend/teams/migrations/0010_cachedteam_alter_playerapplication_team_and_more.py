# Generated by Django 4.2 on 2024-12-01 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("teams", "0009_alter_transferrequest_player_alter_team_options_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="CachedTeam",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("teams.team",),
        ),
        migrations.AlterField(
            model_name="playerapplication",
            name="team",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="applications",
                to="teams.cachedteam",
            ),
        ),
        migrations.AlterField(
            model_name="transferrequest",
            name="from_team",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="transfers_out",
                to="teams.cachedteam",
            ),
        ),
        migrations.AlterField(
            model_name="transferrequest",
            name="to_team",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="transfers_in",
                to="teams.cachedteam",
            ),
        ),
    ]