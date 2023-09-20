from django.db import models


class UserProfule(models.Model):
    user_id = models.IntegerField()
    user_login = models.CharField(max_length=255, blank=True)
    user_name = models.CharField(max_length=255, blank=True)
    user_last_name = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    subscription = models.BooleanField(default=False)
    bonus_awarded = models.BooleanField(default=False)
    mark = models.CharField(max_length=260, default='')

    def __str__(self):
        return f"{self.user_id} - {self.user_name}"
