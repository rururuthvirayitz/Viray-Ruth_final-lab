from email.policy import default

from django.db import models
from django.urls import reverse


class AcademicEvent(models.Model):
    month = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField()
    event = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.event} ({self.month})"

    def get_absolute_url(self):
        return reverse("academicevent_detail", kwargs={"pk": self.pk})


class Dashboard(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("announcement_detail", kwargs={"pk": self.pk})

class Files(models.Model):
    FILE_TYPES = [
        ('pdf', 'PDF'),
        ('book', 'Book'),
        ('file', 'File'),
    ]
    SUBJECT_CHOICES = [
        ('Math', 'Mathematics'),
        ('Science', 'Science'),
        ('English', 'English'),
        ('History', 'History'),
        ('IT', 'Information Technology'),
        ('PE', 'Physical Education'),
        ('Arts', 'Arts'),
        ('Music', 'Music'),
    ]

    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=50, choices=SUBJECT_CHOICES, default='Math')
    file = models.FileField(upload_to='files/')
    file_type = models.CharField(max_length=10, choices=FILE_TYPES)
    uploaded_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.get_subject_display()})"

    def get_absolute_url(self):
        return reverse("files_detail", kwargs={"pk": self.pk})


class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(
        max_length=10,
        choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')],
        default='Male'
    )
    birthdate = models.DateField()
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    grade = models.PositiveIntegerField()
    address = models.TextField()
    guardian_name = models.CharField(max_length=255)
    nationality = models.CharField(max_length=50)
    student_number = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.email})'


class Admission(models.Model):
    student_id = models.ForeignKey('Student', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255)
    student_number = models.CharField(max_length=50, unique=True)
    grade = models.PositiveIntegerField(default=1)

    address = models.TextField()
    birthdate = models.DateField()
    email = models.EmailField(unique=True)
    emergency_contact = models.CharField(max_length=15)
    gender = models.CharField(
        max_length=10,
        choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')],
        default='Male'
    )

    guardian_name = models.CharField(max_length=255)
    nationality = models.CharField(max_length=50)
    status = models.CharField(
        max_length=20,
        choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')],
        default='Pending'
    )
    enroll_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.status})"

    def get_absolute_url(self):
        return reverse("admission_detail", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        if self.status == "Approved" and not self.student_id:

            student, created = Student.objects.get_or_create(
                student_number=self.student_number,
                defaults={
                    'first_name': self.name.split()[0],
                    'last_name': self.name.split()[1],
                    'email': self.email,
                    'gender': self.gender,
                    'birthdate': self.birthdate,
                    'contact_number': self.emergency_contact,
                    'grade': self.grade,
                    'address': self.address,
                    'guardian_name': self.guardian_name,
                    'nationality': self.nationality
                }
            )
            self.student_id = student

        super().save(*args, **kwargs)


class List(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("announcement_detail", kwargs={"pk": self.pk})





class Teacher(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    email = models.EmailField()
    gender = models.CharField(max_length=10)  # Male, Female, Other
    age = models.IntegerField()
    address = models.TextField()
    date_of_birth = models.DateField()



    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse("teacher_list", kwargs={"pk": self.pk})





class Calendar(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    category = models.CharField(max_length=200)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("calendar_list", kwargs={"pk": self.pk})

class Announcement(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=200, blank=True, null=True)
    body = models.TextField(max_length=200)
    created_by = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    visibility = models.IntegerField(choices=[(1, 'All'), (2, 'Students'), (3, 'Teachers'), (4, 'Parents')])

    def __str__(self):
        return self.title

class CalendarEvent(models.Model):
    event_name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.event_name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    content = models.TextField(max_length=200, blank=True, null=True)
    isbn = models.CharField(max_length=13, unique=True)
    copies_available = models.IntegerField()

    def __str__(self):
        return self.title

    def get_subject_display(self):
        return dict(self.SUBJECT_CHOICES).get(self.subject, self.subject)


class Admission(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    name = models.CharField(max_length=255)
    grade = models.CharField(max_length=10)
    student_number = models.CharField(max_length=20)
    birthdate = models.DateField(default="2000-01-01")
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='Male')
    address = models.TextField(null=True, blank=True)
    guardian_name = models.CharField(max_length=255, default='<NAME>')
    emergency_contact = models.CharField(max_length=20, default="00000000")
    nationality = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')


    def __str__(self):
        return self.name


class Personnel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    position = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=100)
    gender = models.CharField(max_length=50)
    age = models.IntegerField()
    address = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"