from django import forms
from .models import Student, Teacher, Parent, Announcement, Book


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'grade_level', 'date_of_birth']


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'subject', 'department']
        widgets = {}

class  ParentsForm(forms.ModelForm):
    class Meta:
        model = Parent
        fields = ['first_name', 'last_name']
        widgets = {}

class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'content']
        widgets = {}
        labels = {
            'title': 'Title',
        }

class BooksForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'copies_available']
        widgets = {}

