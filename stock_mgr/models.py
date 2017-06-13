from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from time import time

def get_upload_file_name(instance, filename):
    return "uploaded_files/%s_%s" % (str(time()).replace('.','_'), filename)


class StoreItem(models.Model):
	itemName       = models.CharField(max_length = 40)
	itemCode       = models.CharField(max_length = 40)
	description    = models.TextField(max_length = 1000)
	quantity        = models.IntegerField()
	date_delivered = models.DateTimeField(auto_now_add = True)
	date_restocked = models.DateTimeField(auto_now_add = False, auto_now=True)
	added_by       = models.ForeignKey(User)

	def __unicode__(self):
		return self.itemName 

class UserAccount(models.Model):
	user           = models.ForeignKey(User, on_delete=models.CASCADE,)
	gender         = models.CharField(max_length = 40)
	phoneNumber    = models.CharField(max_length = 40)
	dob            = models.DateField(default=None)
	thumbnail      = models.FileField(upload_to  = get_upload_file_name, default='static/assets/img/find_user.png')
	address        = models.CharField(max_length = 200, default=None)
	state          = models.CharField(max_length = 40, default=None)
	country        = models.CharField(max_length = 40, default=None)
	#manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE,)
	

	def __unicode__(self):
		return self.user.username 
