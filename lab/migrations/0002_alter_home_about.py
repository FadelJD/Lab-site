# Generated by Django 4.2 on 2023-04-17 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='about',
            field=models.CharField(max_length=500),
        ),
    ]
