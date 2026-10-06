from django.db import models
from django.contrib import admin
class customer_DB(models.Model):
    Name=models.CharField(max_length=20)
    Mobile_num=models.IntegerField()
    vechile_colour=models.CharField(max_length=20)
    Service_no=models.IntegerField()
    Service_mode=models.CharField(max_length=20)
    Amountbill_no=models.IntegerField()
    email=models.CharField(max_length=30)
class customer_DBAdmin(admin.ModelAdmin):
    list_display=["Name","Mobile_num","vechile_colour","Service_no","Service_mode","Amountbill_no","email"]