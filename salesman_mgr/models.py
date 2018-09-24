from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class SalesStock(models.Model):
	user           = models.ForeignKey(User)
	itemName       = models.CharField(max_length = 40)
	itemCode       = models.CharField(max_length = 40)
	quantity       = models.IntegerField()
	unit_price     = models.IntegerField()
	date_added     = models.DateTimeField(auto_now_add = True)
	date_restocked = models.DateTimeField(auto_now_add = False, auto_now=True)
	#add_by       = models.ForeignKey(User)

	def __unicode__(self):
		return self.user 