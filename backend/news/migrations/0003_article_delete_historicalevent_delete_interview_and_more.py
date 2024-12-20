# Generated by Django 4.2 on 2024-12-01 13:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("news", "0002_rename_description_historicalevent_event_description_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Article",
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
                ("title", models.CharField(max_length=200)),
                ("content", models.TextField()),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="news_images/"),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "article_type",
                    models.CharField(
                        choices=[
                            ("NEWS", "News"),
                            ("INTERVIEW", "Interview"),
                            ("BLOG", "Blog Post"),
                        ],
                        max_length=10,
                    ),
                ),
                ("is_published", models.BooleanField(default=False)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="articles",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="HistoricalEvent",
        ),
        migrations.DeleteModel(
            name="Interview",
        ),
        migrations.DeleteModel(
            name="NewsPost",
        ),
        migrations.CreateModel(
            name="CachedArticle",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("news.article",),
        ),
    ]
