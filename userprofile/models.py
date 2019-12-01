from django.db import models

class UsrProfile(models.Model):
    username = models.TextField(max_length=20, null=True)
    password = models.TextField(max_length=20, null=True)
    worknum = models.IntegerField(null=True)
    getindate = models.DateTimeField(null=True)
    isadmin = models.IntegerField(null=True)
    class Meta:
        db_table = 'UserProfile'
        ordering = ('-worknum',)

    def __str__(self):
        return str(self.username)