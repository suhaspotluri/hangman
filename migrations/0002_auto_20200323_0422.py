# Generated by Django 3.0.2 on 2020-03-23 04:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hangman', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='difficulty',
            old_name='wordLenMin',
            new_name='wordLenMint',
        ),
    ]