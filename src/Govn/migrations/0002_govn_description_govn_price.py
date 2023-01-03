# Generated by Django 4.1.4 on 2022-12-27 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Govn', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='govn',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='govn',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
            preserve_default=False,
        ),
    ]