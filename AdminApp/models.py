from django.db import models

# users model here
class Users(models.Model):
    name = models.CharField(max_length=210, null=True, blank=True)
    email = models.CharField(max_length=120, null=True, blank=True)
    password = models.CharField(max_length=120, null=True, blank=True)
    user_dept = models.CharField(max_length=120, null=True, blank=True)
    designation = models.CharField(max_length=120, null=True, blank=True)
    work = models.CharField(max_length=120, null=True, blank=True)
    is_active = models.IntegerField()

    class Meta:
        db_table = 'skroman_users'