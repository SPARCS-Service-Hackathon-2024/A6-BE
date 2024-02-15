# Generated by Django 3.2 on 2024-02-15 20:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("diary", "0004_diary_farm_image"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Comment",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("description", models.TextField()),
                (
                    "diary",
                    models.ForeignKey(
                        help_text="일지",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="diary.diary",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        help_text="일지",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]