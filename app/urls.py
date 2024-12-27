from django.urls import path
from .views import (HomePageView, AboutPageView, BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView,
                    StudentListView, StudentCreateView, StudentDetailView, StudentUpdateView, StudentDeleteView,
                    ParentListView, ParentCreateView, ParentDetailView, ParentUpdateView, ParentDeleteView,
                    TeacherListView, TeacherCreateView, TeacherDetailView, TeacherUpdateView, TeacherDeleteView,
                    AnnouncementListView, AnnouncementCreateView, AnnouncementDetailView, AnnouncementUpdateView, AnnouncementDeleteView,
                    BookListView, BookCreateView, BookDetailView, BookUpdateView, BookDeleteView
                    )

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('blog/', BlogListView.as_view(), name='blog'),
    path('blog/<int:pk>', BlogDetailView.as_view(), name='blog_detail'),
    path('blog/create', BlogCreateView.as_view(), name='blog_create'),
    path('blog/<int:pk>/edit', BlogUpdateView.as_view(), name='blog_update'),
    path('blog/<int:pk>/delete', BlogDeleteView.as_view(), name='blog_delete'),

    path('student/', StudentListView.as_view(), name='student'),
    path('student/<int:pk>/', StudentDetailView.as_view(), name='student_detail'),
    path('student/create/', StudentCreateView.as_view(), name='student_create'),
    path('student/<int:pk>/edit/', StudentUpdateView.as_view(), name='student_update'),
    path('student/<int:pk>/delete/', StudentDeleteView.as_view(), name='student_delete'),

    path('parent/', ParentListView.as_view(), name='parent'),
    path('parent/<int:pk>/', ParentDetailView.as_view(), name='parent_detail'),
    path('parent/create/', ParentCreateView.as_view(), name='parent_create'),
    path('parent/<int:pk>/edit/', ParentUpdateView.as_view(), name='parent_update'),
    path('parent/<int:pk>/delete/', ParentDeleteView.as_view(), name='parent_delete'),

    path('teacher/', TeacherListView.as_view(), name='teacher'),
    path('teacher/<int:pk>/', TeacherDetailView.as_view(), name='teacher_detail'),
    path('teacher/create/', TeacherCreateView.as_view(), name='teacher_create'),
    path('teacher/<int:pk>/edit/', TeacherUpdateView.as_view(), name='teacher_update'),
    path('teacher/<int:pk>/delete/', TeacherDeleteView.as_view(), name='teacher_delete'),

    path('announcement/',  AnnouncementListView.as_view(), name='announcement'),
    path('announcement/<int:pk>/',  AnnouncementDetailView.as_view(), name='announcement_detail'),
    path('announcement/create/',  AnnouncementCreateView.as_view(), name='announcement_create'),
    path('announcement/<int:pk>/edit/',  AnnouncementUpdateView.as_view(), name='announcement_update'),
    path('announcement/<int:pk>/delete/',  AnnouncementDeleteView.as_view(), name='announcement_delete'),


    path('book/',  BookListView.as_view(), name='book'),
    path('book/<int:pk>/',  BookDetailView.as_view(), name='book_detail'),
    path('book/create/',  BookCreateView.as_view(), name='book_create'),
    path('book/<int:pk>/edit/',  BookUpdateView.as_view(), name='book_update'),
    path('book/<int:pk>/delete/',  BookDeleteView.as_view(), name='book_delete'),


]