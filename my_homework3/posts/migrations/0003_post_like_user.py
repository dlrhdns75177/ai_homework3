# Generated by Django 4.2 on 2025-01-20 13:29

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("posts", "0002_alter_post_author_comment"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="like_user",
            field=models.ManyToManyField(
                related_name="like_posts", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]