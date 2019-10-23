from django.db import models
from django.utils import timezone

class biodata(models.Model):
	name= models.CharField(max_length=300)
	email= models.EmailField()
	publish = models.DateTimeField(default=timezone.now)


	def __str__(self):
		return self.name
