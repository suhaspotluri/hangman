# Generated by Django 3.0.2 on 2020-03-23 04:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hangman', '0002_auto_20200323_0422'),
    ]

    operations = [
        migrations.RenameField(
            model_name='difficulty',
            old_name='wordLenMint',
            new_name='wordLenMin',
        ),
    ]
