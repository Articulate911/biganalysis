# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class PeopleRequest(models.Model):
    id = models.IntegerField(db_column='id', primary_key=True)
    report_num = models.IntegerField(db_column='REPORT_NUM', null=True)
    event_property_name = models.TextField(db_column='EVENT_PROPERTY_NAME', null=True)  
    event_type_id = models.IntegerField(db_column='EVENT_TYPE_ID', null=True)
    event_type_name = models.TextField(db_column='EVENT_TYPE_NAME', null=True)  
    event_src_name = models.TextField(db_column='EVENT_SRC_NAME', null=True)  
    district_id = models.IntegerField(db_column='DISTRICT_ID', null=True)
    intime_archive_num = models.IntegerField(db_column='INTIME_ARCHIVE_NUM', null=True)
    sub_type_id = models.IntegerField(db_column='SUB_TYPE_ID', null=True)  
    district_name = models.TextField(db_column='DISTRICT_NAME', null=True)  
    community_id = models.IntegerField(db_column='COMMUNITY_ID', null=True)  
    rec_id = models.TextField(db_column='REC_ID', null=True)  
    street_id = models.IntegerField(db_column='STREET_ID', null=True)  
    overtime_archive_num = models.IntegerField(db_column='OVERTIME_ARCHIVE_NUM', null=True)  
    operate_num = models.IntegerField(db_column='OPERATE_NUM', null=True)  
    dispose_unit_id = models.IntegerField(db_column='DISPOSE_UNIT_ID', null=True)  
    street_name = models.TextField(db_column='STREET_NAME', null=True)  
    create_time = models.DateTimeField(db_column='CREATE_TIME', null=True)  
    event_src_id = models.IntegerField(db_column='EVENT_SRC_ID', null=True)  
    intime_to_archive_num = models.IntegerField(db_column='INTIME_TO_ARCHIVE_NUM', null=True)  
    sub_type_name = models.TextField(db_column='SUB_TYPE_NAME', null=True)  
    event_property_id = models.IntegerField(db_column='EVENT_PROPERTY_ID', null=True)  
    occur_place = models.TextField(db_column='OCCUR_PLACE', null=True)  
    community_name = models.TextField(db_column='COMMUNITY_NAME', null=True)  
    dispose_unit_name = models.TextField(db_column='DISPOSE_UNIT_NAME', null=True)  
    main_type_name = models.TextField(db_column='MAIN_TYPE_NAME', null=True)  
    main_type_id = models.IntegerField(db_column='MAIN_TYPE_ID', null=True)  

    class Meta:
        db_table = '坪山区-民生诉求数据_完整版'
        ordering = ('-id',)

    def __str__(self):
        return str(self.create_time)
