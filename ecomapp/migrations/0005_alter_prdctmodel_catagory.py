# Generated by Django 3.2.9 on 2022-07-14 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0004_delete_cartmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prdctmodel',
            name='Catagory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ecomapp.catogorymodel'),
        ),
    ]
