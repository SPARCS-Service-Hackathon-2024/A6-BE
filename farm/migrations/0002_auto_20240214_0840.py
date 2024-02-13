# Generated by Django 3.2 on 2024-02-14 08:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("farm", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="farm",
            name="image",
            field=models.TextField(
                blank=True, default="", help_text="밭 이미지", null=True
            ),
        ),
        migrations.AlterField(
            model_name="farm",
            name="user",
            field=models.ForeignKey(
                help_text="유저",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="farm",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
