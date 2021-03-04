from django.db import models

class Contact(models.Model):
	name = models.CharField(max_length=200)	
	address = models.CharField(max_length=300)
	city = models.CharField(max_length=100)
	state = models.CharField(max_length=2)
	zipcode = models.CharField(max_length=10)

	def __str__(self):
		return self.name
