# Generated by Django 4.2.9 on 2024-01-14 00:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0003_alter_product_options_remove_order_user_cart_user_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="parent",
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to="shop.category"
            ),
        ),
    ]