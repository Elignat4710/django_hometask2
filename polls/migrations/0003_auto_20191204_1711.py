# Generated by Django 3.0 on 2019-12-04 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20191203_0903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worktime',
            name='status',
            field=models.IntegerField(choices=[(1, 'New'), (2, 'Approved'), (3, 'Cancelled')], default=1),
        ),
    ]