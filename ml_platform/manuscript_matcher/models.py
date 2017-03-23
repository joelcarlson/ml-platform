from __future__ import unicode_literals

from django.db import models

class Journal(models.Model):
	"""
	Information related to each journal
	"""
	
	journal_name = models.CharField(max_length=100)
	jcr_category = models.CharField(max_length=100)
	jcr_rank = models.CharField(max_length=100)
	jcr_quartile = models.CharField(max_length=100)
	publisher = models.CharField(max_length=100)
	issn = models.CharField(max_length=100)
	eissn = models.CharField(max_length=100)
	jif = models.CharField(max_length=100)

	class Meta:
		ordering = ('journal_name',)
