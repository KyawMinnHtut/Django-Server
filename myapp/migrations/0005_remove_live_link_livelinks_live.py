# Generated by Django 4.1.6 on 2023-02-12 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_live_aimg_alter_live_himg_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='live',
            name='link',
        ),
        migrations.AddField(
            model_name='livelinks',
            name='live',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.live'),
        ),
    ]
