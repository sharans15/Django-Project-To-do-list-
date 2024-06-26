# Generated by Django 4.2.8 on 2024-01-06 10:53

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("task", "0007_students"),
    ]

    operations = [
        migrations.CreateModel(
            name="Owner",
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
                ("name", models.CharField(max_length=100, null=True)),
                ("age", models.TextField(null=True)),
                (
                    "gender",
                    models.DateTimeField(default=django.utils.timezone.now, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="House",
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
                ("name", models.CharField(max_length=100, null=True)),
                ("city", models.CharField(max_length=100, null=True)),
                ("floors", models.CharField(max_length=100, null=True)),
                ("carpetarea", models.CharField(max_length=100, null=True)),
                (
                    "owner",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="task.owner",
                    ),
                ),
            ],
        ),
    ]
