from django import forms
from app1.models import Course
#create your forms here

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        labels = {
            'cname':'COURSE',
            'dur':'DURATION',
            'fee':'FEE',
        }
        widgets = {
            'cname': forms.TextInput(attrs={'class':"form-control"}),
            'dur': forms.NumberInput(attrs={'class':"form-control"}),
            'fee': forms.NumberInput(attrs={'class':"form-control"}),
        }
