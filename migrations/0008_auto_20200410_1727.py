# Generated by Django 3.0.2 on 2020-04-10 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hangman', '0007_category_catname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='wordName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hangman.wordBankWord'),
        ),
    ]
