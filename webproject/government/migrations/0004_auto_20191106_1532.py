# Generated by Django 2.2.6 on 2019-11-06 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('government', '0003_auto_20191106_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peoplerequest',
            name='id',
            field=models.IntegerField(db_column='id', primary_key=True, serialize=False),
        ),
    ]