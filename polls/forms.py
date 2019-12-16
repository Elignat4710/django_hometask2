from django import forms
from .models import Work, WorkTime, WorkPlace


class WorkCreate(forms.ModelForm):
    class Meta:
        model = Work
        fields = ['name', 'com_name']


class WorktimeCreateForm(forms.ModelForm):
    class Meta:
        model = WorkTime
        fields = ['worker', 'work', 'date_start', 'date_end', 'status']


class AssignWorkerForm(forms.ModelForm):
    class Meta:
        model = WorkPlace
        fields = [
            'name',
            'worker_name',
            'work_name',
            'status',
        ]
