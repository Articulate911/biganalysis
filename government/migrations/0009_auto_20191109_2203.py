# Generated by Django 2.2.6 on 2019-11-09 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('government', '0008_auto_20191109_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peoplerequest',
            name='community_id',
            field=models.IntegerField(db_column='COMMUNITY_ID', null=True),
        ),
        migrations.AlterField(
            model_name='peoplerequest',
            name='community_name',
            field=models.TextField(db_column='COMMUNITY_NAME', null=True),
        ),
        migrations.AlterField(
            model_name='peoplerequest',
            name='create_time',
            field=models.DateTimeField(db_column='CREATE_TIME', null=True),
        ),
        migrations.AlterField(
            model_name='peoplerequest',
            name='dispose_unit_id',
            field=models.IntegerField(db_column='DISPOSE_UNIT_ID', null=True),
        ),
        migrations.AlterField(
            model_name='peoplerequest',
            name='dispose_unit_name',
            field=models.TextField(db_column='DISPOSE_UNIT_NAME', null=True),
        ),
        migrations.AlterField(
            model_name='peoplerequest',
            name='district_name',
            field=models.TextField(db_column='DISTRICT_NAME', null=True),
        ),
        migrations.AlterField(
            model_name='peoplerequest',
            name='event_property_id',
            field=models.IntegerField(db_column='EVENT_PROPERTY_ID', null=True),
        ),
        migrations.AlterField(
            model_name='peoplerequest',
            name='event_property_name',
            field=models.TextField(db_column='EVENT_PROPERTY_NAME', null=True),
        ),
        migrations.AlterField(
            model_name='peoplerequest',
            name='event_src_id',
            field=models.IntegerField(db_column='EVENT_SRC_ID', null=True),
        ),
        migrations.AlterField(
            model_name='peoplerequest',
            name='event_src_name',
            field=models.TextField(db_column='EVENT_SRC_NAME', null=True),
        ),
        migrations.AlterField(
            model_name='peoplerequest',
            name='event_type_name',
            field=models.TextField(db_column='EVENT_TYPE_NAME', null=True),
        ),
        migrations.AlterField(
            model_name='peoplerequest',
            name='intime_to_archive_num',
            field=models.IntegerField(db_column='INTIME_TO_ARCHIVE_NUM', null=True),
        ),
        migrations.AlterField(
            model_name='peoplerequest',
            name='main_type_id',
            field=models.IntegerField(db_column='MAIN_TYPE_ID', null=True),
        ),
        migrations.AlterField(
            model_name='peoplerequest',
            name='main_type_name',
            field=models.TextField(db_column='MAIN_TYPE_NAME', null=True),
        ),
        migrations.AlterField(
            model_name='peoplerequest',
            name='occur_place',
            field=models.TextField(db_column='OCCUR_PLACE', null=True),
        ),
        migrations.AlterField(
            model_name='peoplerequest',
            name='operate_num',
            field=models.IntegerField(db_column='OPERATE_NUM', null=True),
        ),
        migrations.AlterField(
            model_name='peoplerequest',
            name='overtime_archive_num',
            field=models.IntegerField(db_column='OVERTIME_ARCHIVE_NUM', null=True),
        ),
        migrations.AlterField(
            model_name='peoplerequest',
            name='rec_id',
            field=models.TextField(db_column='REC_ID', null=True),
        ),
        migrations.AlterField(
            model_name='peoplerequest',
            name='street_id',
            field=models.IntegerField(db_column='STREET_ID', null=True),
        ),
        migrations.AlterField(
            model_name='peoplerequest',
            name='street_name',
            field=models.TextField(db_column='STREET_NAME', null=True),
        ),
        migrations.AlterField(
            model_name='peoplerequest',
            name='sub_type_id',
            field=models.IntegerField(db_column='SUB_TYPE_ID', null=True),
        ),
        migrations.AlterField(
            model_name='peoplerequest',
            name='sub_type_name',
            field=models.TextField(db_column='SUB_TYPE_NAME', null=True),
        ),
    ]