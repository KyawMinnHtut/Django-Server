# Generated by Django 4.1.6 on 2023-02-13 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='desc',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
