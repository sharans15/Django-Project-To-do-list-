# Generated by Django 4.2.8 on 2024-03-23 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("task", "0013_house_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="todo",
            name="image2",
            field=models.ImageField(null=True, upload_to="images2"),
        ),
    ]
