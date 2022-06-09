# Generated by Django 4.0.4 on 2022-05-29 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conversor', '0002_remove_brand_tax_remove_brand_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='tax',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='brand',
            name='value',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='mile',
            name='balance',
            field=models.FloatField(default=0),
        ),
    ]