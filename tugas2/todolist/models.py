from django.db import models

class Todo(models.Model):
	text = models.CharField(max_length=50)
	status = models.BooleanField(default=False)

	def __str__(self):
		return self.text
# Create your models here.
