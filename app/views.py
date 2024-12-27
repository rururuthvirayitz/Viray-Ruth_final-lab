from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post, Student, Teacher, Parent, Announcement, Book
from .forms import StudentForm, TeacherForm, ParentsForm, AnnouncementForm, BooksForm
from django.urls import reverse_lazy

class HomePageView(TemplateView):
    template_name = 'app/home.html'

class AboutPageView(TemplateView):
    template_name = 'app/about.html'

class BlogListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'app/blog_list.html'

class BlogDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'app/blog_detail.html'

class BlogCreateView(CreateView):
    model = Post
    fields = ['title', 'author', 'body']
    template_name = 'app/blog_create.html'

class BlogUpdateView(UpdateView):
    model = Post
    fields = ['title', 'author', 'body']
    template_name = 'app/blog_update.html'

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'app/blog_delete.html'
    success_url = reverse_lazy('home')

class StudentListView(ListView):
    model = Student
    context_object_name = 'students'
    template_name = 'app/student_list.html'

class StudentDetailView(DetailView):
    model = Student
    context_object_name = 'student'
    template_name = 'app/student_detail.html'

class StudentCreateView(CreateView):
    model = Student
    fields = ['first_name', 'last_name', 'middle_name', 'date_of_birth', 'age',
              'gender', 'address', 'parent', 'email', 'parent_phone_number',
              'grade_level']
    template_name = 'app/student_create.html'

class StudentUpdateView(UpdateView):
    model = Student
    fields = ['first_name', 'last_name', 'middle_name', 'date_of_birth', 'age',
              'gender', 'address', 'parent', 'email', 'parent_phone_number',
              'grade_level']
    template_name = 'app/student_update.html'

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'app/student_delete.html'
    success_url = reverse_lazy('student')

class ParentListView(ListView):
    model = Parent
    context_object_name = 'parents'
    template_name = 'app/parent_list.html'

class ParentDetailView(DetailView):
    model = Parent
    context_object_name = 'parent'
    template_name = 'app/parent_detail.html'

class ParentCreateView(CreateView):
    model = Parent
    fields = ['first_name', 'last_name', 'middle_name', 'age',
              'gender', 'address', 'email', 'phone_number', 'student'
              ]
    template_name = 'app/parent_create.html'

class ParentUpdateView(UpdateView):
    model = Parent
    fields = ['first_name', 'last_name', 'middle_name', 'age',
              'gender', 'address', 'email', 'phone_number', 'student']
    template_name = 'app/parent_update.html'

class ParentDeleteView(DeleteView):
    model = Parent
    template_name = 'app/parent_delete.html'
    success_url = reverse_lazy('parent')



class TeacherListView(ListView):
    model = Teacher
    context_object_name = 'teachers'
    template_name = 'app/teacher_list.html'

class TeacherDetailView(DetailView):
    model = Teacher
    context_object_name = 'teacher'
    template_name = 'app/teacher_detail.html'

class TeacherCreateView(CreateView):
    model = Teacher
    fields = ['first_name', 'last_name', 'middle_name', 'date_of_birth', 'age',
              'gender', 'address', 'email', 'phone_number', 'department',
              'subject', 'hire_date', 'employment_status'
              ]
    template_name = 'app/teacher_create.html'

class TeacherUpdateView(UpdateView):
    model = Teacher
    fields = ['first_name', 'last_name', 'middle_name', 'date_of_birth', 'age',
              'gender', 'address', 'email', 'phone_number', 'department',
              'subject', 'hire_date', 'employment_status']
    template_name = 'app/teacher_update.html'

class TeacherDeleteView(DeleteView):
    model = Teacher
    template_name = 'app/teacher_delete.html'
    success_url = reverse_lazy('teacher')




class AnnouncementListView(ListView):
    model = Announcement
    context_object_name = 'announcements'
    template_name = 'app/announcement_list.html'

class AnnouncementDetailView(DetailView):
    model = Announcement
    context_object_name = 'announcement'
    template_name = 'app/announcement_detail.html'

class AnnouncementCreateView(CreateView):
    model = Announcement
    fields = ['title', 'content', 'body', 'created_by', 'visibility'
              ]
    template_name = 'app/announcement_create.html'

class AnnouncementUpdateView(UpdateView):
    model = Announcement
    fields = ['title', 'content', 'body', 'created_by', 'visibility']
    template_name = 'app/announcement_update.html'

class AnnouncementDeleteView(DeleteView):
    model = Announcement
    template_name = 'app/announcement_delete.html'
    success_url = reverse_lazy('announcement')




class BookListView(ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'app/book_list.html'

class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'app/book_detail.html'

class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'author', 'content', 'isbn', 'copies_available'
              ]
    template_name = 'app/book_create.html'

class BookUpdateView(UpdateView):
    model = Book
    fields = ['title', 'author', 'content', 'isbn', 'copies_available']
    template_name = 'app/book_update.html'

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'app/book_delete.html'
    success_url = reverse_lazy('book')