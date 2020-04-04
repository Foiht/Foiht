from django.forms import ModelForm
from .models import Todo, Mail

class TodoForm(ModelForm):
	class Meta:
		model = Todo
		fields = ['title', 'memo', 'important']

class MailForm(ModelForm):
	class Meta:
		model = Mail
		fields = ['title', 'todolist', 'usermail']

