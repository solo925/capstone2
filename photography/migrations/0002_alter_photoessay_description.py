# Generated by Django 5.0.7 on 2024-07-13 08:13

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("photography", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="photoessay",
            name="description",
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
