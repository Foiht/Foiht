from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
	title = models.CharField(max_length=100)
	created = models.DateTimeField(auto_now_add=True)
	memo = models.TextField(max_length=500, blank=True)
	datecompleted = models.DateTimeField(null=True, blank=True)
	important = models.BooleanField(default=False)
	user = models.ForeignKey(User, on_delete=models.CASCADE)


	def __str__(self):
		return self.title


class Mail(models.Model):
	title = models.CharField(max_length=100)
	todolist = models.TextField(max_length=1000, blank=True)
	usermail = models.CharField(max_length=100)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title