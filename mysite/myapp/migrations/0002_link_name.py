# Generated by Django 5.0.7 on 2024-07-20 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
