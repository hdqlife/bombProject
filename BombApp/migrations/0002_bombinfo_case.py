# Generated by Django 3.0.2 on 2020-05-27 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BombApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bombinfo',
            name='case',
            field=models.CharField(default=1, max_length=256),
            preserve_default=False,
        ),
    ]