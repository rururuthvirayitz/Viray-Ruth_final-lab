from tkinter.font import names
from xml.etree.ElementInclude import include
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .views import (HomePageView, AboutPageView, EnrollmentPageView, CustomLoginView, admin_dashboard, admin_files,
                    AcademicEventListView, AcademicEventCreateView, AcademicEventDetailView, AcademicEventUpdateView, AcademicEventDeleteView,
                    AnnouncementListView, AnnouncementCreateView, AnnouncementDetailView, AnnouncementUpdateView, AnnouncementDeleteView,
                    BookListView,
                    CalendarListView, DashboardListView,
                    FilesListView, FilesCreateView, FilesDeleteView, FilesUpdateView, FilesDetailView,
                    AdmissionListView, AdmissionDetailView, AdmissionCreateView, AdmissionDeleteView, AdmissionUpdateView,
                    ListListView,
                    CalendarEventListView, CalendarEventDetailView, CalendarEventCreateView,
                    CalendarEventUpdateView, CalendarEventDeleteView,
                    TeacherListView, TeacherDetailView, TeacherCreateView, TeacherUpdateView, TeacherDeleteView,
                    PersonnelListView, PersonnelCreateView, PersonnelUpdateView, PersonnelDeleteView, PersonnelDetailView,
                    CalendarListView,
                    )

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('enrollment/', EnrollmentPageView.as_view(), name='enrollment'),

    path('login/', CustomLoginView.as_view(), name='login'),
    # Custom login
    path('admin/dashboard/', admin_dashboard, name='dashboard'),
    path('admin/files/', admin_files, name='files'),
    path('enrollment/create/', views.EnrollmentCreateView.as_view(), name='enrollment_create'),


    path('calendar/', CalendarListView.as_view(), name='calendar_list'),

    path('academicevent/', AcademicEventListView.as_view(), name='academicevent'),
    path('academicevent/<int:pk>/', AcademicEventDetailView.as_view(), name='academicevent_detail'),
    path('academicevent/create/', AcademicEventCreateView.as_view(), name='academicevent_create'),
    path('academicevent/<int:pk>/edit/', AcademicEventUpdateView.as_view(), name='academicevent_update'),
    path('academicevent/<int:pk>/delete/', AcademicEventDeleteView.as_view(), name='academicevent_delete'),

    path('calendar_event/', CalendarEventListView.as_view(), name='calendar_event'),
    path('calendar_event/<int:pk>/', CalendarEventDetailView.as_view(), name='calendar_event_detail'),
    path('calendar_event/create/', CalendarEventCreateView.as_view(), name='calendar_event_create'),
    path('calendar_event/<int:pk>/edit/', CalendarEventUpdateView.as_view(), name='calendar_event_update'),
    path('calendar_event/<int:pk>/delete/', CalendarEventDeleteView.as_view(), name='calendar_event_delete'),

    path('announcements/',  AnnouncementListView.as_view(), name='announcement'),
    path('announcement/<int:pk>/',  AnnouncementDetailView.as_view(), name='announcement_detail'),
    path('announcement/create/',  AnnouncementCreateView.as_view(), name='announcement_create'),
    path('announcement/<int:pk>/edit/',  AnnouncementUpdateView.as_view(), name='announcement_update'),
    path('announcement/<int:pk>/delete/',  AnnouncementDeleteView.as_view(), name='announcement_delete'),

    path('personnel/', views.PersonnelListView.as_view(), name='personnel'),  # List all personnel
    path('personnel/<int:pk>/',  views.PersonnelDetailView.as_view(), name='personnel_detail'),
    path('personnel/create/', views.PersonnelCreateView.as_view(), name='personnel_create'),  # Create personnel
    path('personnel/<int:pk>/update/', views.PersonnelUpdateView.as_view(), name='personnel_update'),
    path('personnel/<int:pk>/delete/', views.PersonnelDeleteView.as_view(), name='personnel_delete'),

    # Delete personnel

    path('book/',  BookListView.as_view(), name='book'),



    path('calendar/', CalendarListView.as_view(), name='calendar'),
    path('dashboard/', DashboardListView.as_view(), name='dashboard'),


    path('files/', FilesListView.as_view(), name='files'),
    path('files/<int:pk>/',  FilesDetailView.as_view(), name='files_detail'),
    path('files/create/',  FilesCreateView.as_view(), name='files_create'),
    path('files/<int:pk>/edit/',  FilesUpdateView.as_view(), name='files_update'),
    path('files/<int:pk>/delete/',  FilesDeleteView.as_view(), name='files_delete'),

    path('admission/', AdmissionListView.as_view(), name='admission'),
    path('admission/<int:pk>/', AdmissionDetailView.as_view(), name='admission_detail'),
    path('admission/create/', AdmissionCreateView.as_view(), name='admission_create'),
    path('admission/<int:pk>/edit/', AdmissionUpdateView.as_view(), name='admission_update'),
    path('admission/<int:pk>/delete/', AdmissionDeleteView.as_view(), name='admission_delete'),


    path('list/', ListListView.as_view(), name='list'),



    # Teachers URLs
    path('teachers/', TeacherListView.as_view(), name='teachers'),
    path('teacher/<int:pk>/', TeacherDetailView.as_view(), name='teacher_detail'),
    path('teacher/create/', TeacherCreateView.as_view(), name='teacher_create'),
    path('teacher/<int:pk>/update/', TeacherUpdateView.as_view(), name='teacher_update'),
    path('teacher/<int:pk>/delete/', TeacherDeleteView.as_view(), name='teacher_delete'),



]
