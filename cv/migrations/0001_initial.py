# Generated by Django 5.0.7 on 2024-07-10 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CV",
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
                (
                    "language",
                    models.CharField(
                        choices=[
                            ("english", "English"),
                            ("kiswahili", "Kiswahili"),
                            ("indigenous", "Indigenous"),
                        ],
                        max_length=20,
                    ),
                ),
                ("file", models.FileField(upload_to="cv/")),
                ("uploaded_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
