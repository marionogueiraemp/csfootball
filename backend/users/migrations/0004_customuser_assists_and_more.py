# Generated by Django 5.1.3 on 2024-11-30 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_customuser_is_player"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="assists",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="customuser",
            name="email_verification_token",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="customuser",
            name="email_verified",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="customuser",
            name="goals_scored",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="customuser",
            name="matches_played",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="customuser",
            name="red_cards",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="customuser",
            name="steam_id",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="customuser",
            name="steam_profile_url",
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name="customuser",
            name="yellow_cards",
            field=models.IntegerField(default=0),
        ),
    ]
