# Generated by Django 4.2.8 on 2024-03-23 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("task", "0012_alter_blog_blogger_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="house",
            name="image",
            field=models.ImageField(null=True, upload_to="images"),
        ),
    ]