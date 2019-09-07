# Generated by Django 2.2 on 2019-09-07 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventFinderApp', '0004_auto_20190907_1010'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='event',
            field=models.ManyToManyField(to='eventFinderApp.Event'),
        ),
        migrations.AlterField(
            model_name='event',
            name='venue',
            field=models.CharField(max_length=200, null='True'),
        ),
    ]
