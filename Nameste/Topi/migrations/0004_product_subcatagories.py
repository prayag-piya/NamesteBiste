# Generated by Django 3.0.6 on 2020-05-26 10:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Topi', '0003_auto_20200526_0809'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='subcatagories',
            field=models.CharField(choices=[('J', 'JACKET'), ('T', 'TSHRIT'), ('S', 'SHRIT')], default=django.utils.timezone.now, max_length=2),
            preserve_default=False,
        ),
    ]
