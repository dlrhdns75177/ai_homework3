# Generated by Django 4.2 on 2025-01-15 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_profile"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="image",
            field=models.ImageField(blank=True, upload_to="images/"),
        ),
    ]