# Generated by Django 4.1.6 on 2023-02-14 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0003_series_premium_alter_series_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('link', models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='part',
            name='downloadLink',
        ),
        migrations.RemoveField(
            model_name='part',
            name='playLink',
        ),
        migrations.AddField(
            model_name='part',
            name='playLink',
            field=models.ManyToManyField(blank=True, to='series.link'),
        ),
    ]
