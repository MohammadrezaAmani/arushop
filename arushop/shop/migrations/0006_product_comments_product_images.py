# Generated by Django 4.2.9 on 2024-01-18 22:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("other", "0001_initial"),
        ("shop", "0005_delete_comment"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="comments",
            field=models.ManyToManyField(blank=True, related_name="comments", to="other.comment"),
        ),
        migrations.AddField(
            model_name="product",
            name="images",
            field=models.ManyToManyField(blank=True, related_name="images", to="other.image"),
        ),
    ]
