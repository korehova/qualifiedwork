# Generated by Django 4.1.7 on 2023-04-24 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mycloud", "0005_alter_file_users"),
    ]

    operations = [
        migrations.AlterField(
            model_name="file", name="file", field=models.FileField(upload_to=""),
        ),
    ]
