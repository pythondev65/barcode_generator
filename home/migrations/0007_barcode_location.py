# Generated by Django 3.2.9 on 2021-11-16 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20211116_1503'),
    ]

    operations = [
        migrations.AddField(
            model_name='barcode',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.location'),
        ),
    ]
