# Generated by Django 4.1.6 on 2023-02-14 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('highlights', '0002_remove_highlight_time_highlight_premium_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='highlight',
            name='link',
            field=models.ManyToManyField(blank=True, to='highlights.highlightlink'),
        ),
    ]
