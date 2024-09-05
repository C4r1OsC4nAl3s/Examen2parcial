from django import forms
from django.contrib.auth.models import User
from datetime import date


CHOICES_STATUS = [
    ("DONE", "Finished"),
    ("PEND", "Pending"),
    ("UNDO", "Undone"),
]

class TaskForm(forms.Form):
    title = forms.CharField(max_length=80, label='Title')
    description = forms.CharField(max_length=250, label='Description', widget=forms.Textarea)
    created_at = forms.DateField(label='Created At', initial=date.today, widget=forms.DateInput(attrs={'type': 'date'}))
    due_date = forms.DateField(label='Due Date', widget=forms.DateInput(attrs={'type': 'date'}))
    status = forms.ChoiceField(choices=CHOICES_STATUS, label='Status')
    userID = forms.ModelChoiceField(queryset=User.objects.all(), label='User')  

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['created_at'].initial = date.today()
        
    def clean_userID(self):
        userID = self.cleaned_data['userID'].id
        return userID
