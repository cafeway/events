from django.db import models
from django import forms
# Create your models here.
from django.core.urlresolvers import reverse

class events(models.Model):
	name=models.CharField(max_length=30)
	location=models.CharField(max_length=40)
	date=models.DateField()
	
	def __str__(self):
		return self.name






