# Generated by Django 2.2.6 on 2019-11-06 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('government', '0005_auto_20191106_1535'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='peoplerequest',
            options={'ordering': ('id',)},
        ),
    ]
