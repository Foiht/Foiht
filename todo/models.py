from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
	title = models.CharField(max_length=100)
	created = models.DateTimeField(auto_now_add=True)
	memo = models.TextField(max_length=500, blank=True)
	datecompleted = models.DateTimeField(null=True)
	important = models.BooleanField(default=False)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
