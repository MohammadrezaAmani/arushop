# Generated by Django 4.2.8 on 2024-01-14 06:45

from django.db import migrations, models
import markdownfield.models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0002_alter_slider_time"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="config",
            name="value",
        ),
        migrations.AddField(
            model_name="config",
            name="about",
            field=markdownfield.models.MarkdownField(blank=True, null=True, rendered_field="about_rendered"),
        ),
        migrations.AddField(
            model_name="config",
            name="about_rendered",
            field=markdownfield.models.RenderedMarkdownField(null=True),
        ),
        migrations.AddField(
            model_name="config",
            name="site_url",
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name="config",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="config",
            name="name",
            field=models.CharField(max_length=256),
        ),
    ]
