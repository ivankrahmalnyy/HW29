# Generated by Django 4.1.1 on 2022-10-08 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_alter_user_role"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="location",
            new_name="locations",
        ),
    ]