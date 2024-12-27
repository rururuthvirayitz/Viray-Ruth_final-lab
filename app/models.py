from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"pk": self.pk})

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    age = models.IntegerField(null=True, blank=True)
    gender = models.IntegerField(choices=[(1, 'Male'), (2, 'Female')])
    address = models.TextField(null=True, blank=True)
    parent = models.ForeignKey('Parent', on_delete=models.SET_NULL, null=True, blank=True, related_name='students')
    email = models.EmailField(blank=True, null=True)
    parent_phone_number = models.CharField(max_length=15)
    grade_level = models.IntegerField(choices=[(1, 'Grade 1'), (2, 'Grade 2'), (3, 'Grade 3'),
                                               (4, 'Grade 4'), (5, 'Grade 5'), (6, 'Grade 6')])

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse("student_detail", kwargs={"pk": self.pk})


class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    age = models.IntegerField(null=True, blank=True)
    gender = models.IntegerField(choices=[(1, 'Male'), (2, 'Female')])
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=15)
    address = models.TextField(blank=True, null=True)
    department = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    hire_date = models.DateField(blank=True, null=True)
    employment_status = models.IntegerField(choices=[(1, 'Full Time'), (2, 'Part Time'), (3, 'Contractual')])

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse("teacher_detail", kwargs={"pk": self.pk})

class Parent(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    age = models.IntegerField(null=True, blank=True)
    gender = models.IntegerField(choices=[(1, 'Male'), (2, 'Female')])
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=15)
    address = models.TextField(blank=True, null=True)
    student = models.ForeignKey('Student', on_delete=models.SET_NULL, null=True, blank=True, related_name='parents')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse("parent_detail", kwargs={"pk": self.pk})

class Announcement(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=200, blank=True, null=True)
    body = models.TextField(max_length=200)
    created_by = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    visibility = models.IntegerField(choices=[(1, 'All'), (2, 'Students'), (3, 'Teachers'), (4, 'Parents')])

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("announcement_detail", kwargs={"pk": self.pk})

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    content = models.TextField(max_length=200, blank=True, null=True)
    isbn = models.CharField(max_length=13, unique=True)
    copies_available = models.IntegerField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"pk": self.pk})