# Generated by Django 3.2 on 2024-02-16 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_user_farm_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="farm_image",
            field=models.TextField(
                blank=True,
                default="/media/farms/a49b542a35ce48e6979c92265d84ed2e.png",
                help_text="나의 밭 이미지",
                null=True,
            ),
        ),
    ]
