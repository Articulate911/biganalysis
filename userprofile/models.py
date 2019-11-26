from django.db import models

class UsrProfile(models.Model):
    id = models.IntegerField(db_column='id', primary_key=True)
    username = models.TextField(max_length=20, null=True)
    password = models.TextField(max_length=20, null=True)

    class Meta:
        db_table = 'UserProfile'
        ordering = ('-id',)

    def __str__(self):
        return str(self.username)