from django import forms
from .models import (Announcement, Book, AcademicEvent, Calendar, Dashboard, Files, Admission,
                     List, Teacher, CalendarEvent, Personnel )


class DashboardForm(forms.ModelForm):
    class Meta:
        model = Dashboard
        fields = '__all__'
        widgets = {

        }

class FilesForm(forms.ModelForm):
    class Meta:
        model = Files
        fields = ['name', 'subject', 'file', 'file_type']





class AdmissionForm(forms.ModelForm):
    class Meta:
        model = Admission
        fields = ['name', 'grade', 'student_number', 'birthdate', 'gender', 'address', 'guardian_name',
                  'emergency_contact', 'nationality', 'email']

class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = '__all__'
        widgets = {}

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Admission  # Use Admission model directly here
        fields = ['name', 'grade', 'student_number', 'gender', 'birthdate', 'address', 'guardian_name', 'emergency_contact', 'nationality', 'email', 'status']

class CalendarEventForm(forms.ModelForm):
    class Meta:
        model = AcademicEvent
        fields = '__all__'
        widgets = {

        }


class AcademicForm(forms.ModelForm):
    class Meta:
        model = Calendar
        fields = '__all__'
        widgets = {}

class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'content', 'created_by', 'visibility']


class BooksForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'copies_available']
        widgets = {}



class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'
        widgets = {}
        labels = {}



class CalendarEventForm(forms.ModelForm):
    class Meta:
        model = CalendarEvent
        fields = ['event_name', 'start_date', 'end_date', 'description']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'end_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class PersonnelForm(forms.ModelForm):
    class Meta:
        model = Personnel
        fields = ['first_name', 'last_name', 'email', 'position', 'employee_id', 'gender', 'age', 'address']
        widgets = {
            'gender': forms.Select(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')]),
        }