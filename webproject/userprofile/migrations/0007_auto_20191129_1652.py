# Generated by Django 2.2.7 on 2019-11-29 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0006_auto_20191127_1412'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usrprofile',
            options={'ordering': ('-worknum',)},
        ),
        migrations.AddField(
            model_name='usrprofile',
            name='isadmin',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='usrprofile',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
