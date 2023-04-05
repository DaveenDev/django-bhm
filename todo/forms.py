from django import forms
  
from .models import Task
  
class TaskForm(forms.ModelForm):
      title = forms.CharField(max_length=200, widget= forms.Textarea(attrs={'placeholder':'Enter new task here. . .'}))
  
      class Meta:
          model = Task
          fields = '__all__'