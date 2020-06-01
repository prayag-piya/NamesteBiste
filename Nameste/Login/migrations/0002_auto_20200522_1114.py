# Generated by Django 3.0.6 on 2020-05-22 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='birth_date',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='location',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='user',
        ),
        migrations.AddField(
            model_name='signup',
            name='address',
            field=models.CharField(default='prayag', max_length=80),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='signup',
            name='email',
            field=models.EmailField(default='prayagpiya12@gmail.com', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='signup',
            name='fname',
            field=models.CharField(default='prayag', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='signup',
            name='lname',
            field=models.CharField(default='piya', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='signup',
            name='password',
            field=models.CharField(default='psdasd', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='signup',
            name='postalcode',
            field=models.CharField(default='df', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='signup',
            name='streetno',
            field=models.CharField(default='wew', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='signup',
            name='username',
            field=models.CharField(default='prayag', max_length=30),
            preserve_default=False,
        ),
    ]