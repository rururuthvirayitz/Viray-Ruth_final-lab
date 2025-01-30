from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from datetime import datetime
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Announcement, Book, AcademicEvent, Calendar, Dashboard, Files, Admission, Personnel, List, Teacher, CalendarEvent
from .forms import AnnouncementForm, BooksForm, DashboardForm, PersonnelForm, FilesForm, EnrollmentForm, ListForm, TeacherForm, CalendarEventForm
from django.urls import reverse_lazy


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'  # Specify your login template

    def get_success_url(self):
        # Redirect based on the user's role
        if self.request.user.is_staff or self.request.user.is_superuser:
            return redirect('dashboard')  # Admin dashboard
        else:
            return redirect('studhome')  # Student home

def admin_dashboard(request):
    return render(request, 'app/dashboard_list.html')  # Admin-specific template


def admin_files(request):
    return render(request, 'app/files_list.html')


class DashboardListView(ListView):
    template_name = 'app/dashboard_list.html'
    context_object_name = 'dashboard_data'

    def get_queryset(self):
        # Return an empty queryset or None since we're not using a specific model.
        return []

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Fetch dashboard data
        context['announcements'] = Announcement.objects.all().order_by('-id')[:5]  # Fetch latest 5 announcements
        context['events'] = CalendarEvent.objects.all().order_by('-start_date')[:5]

        # Count total records
        context['teacher_count'] = Teacher.objects.count()
        context['personnel_count'] = Personnel.objects.count()
        context['admission_count'] = Admission.objects.count()

        return context


class PersonnelListView(ListView):
    model = Personnel
    template_name = 'app/personnel_list.html'
    context_object_name = 'personnel'

class PersonnelDetailView(DetailView):
    model = Personnel
    context_object_name = 'personnel'
    template_name = 'app/personnel_detail.html'

# Create View for Personnel
class PersonnelCreateView(CreateView):
    model = Personnel
    form_class = PersonnelForm
    template_name = 'app/personnel_create.html'
    success_url = reverse_lazy('personnel')  # Redirect to personnel list after success

# Update View for Personnel
class PersonnelUpdateView(UpdateView):
    model = Personnel
    form_class = PersonnelForm
    template_name = 'app/personnel_update.html'
    success_url = reverse_lazy('personnel')  # Redirect to personnel list after success

# Delete View for Personnel
class PersonnelDeleteView(DeleteView):
    model = Personnel
    template_name = 'app/personnel_delete.html'
    success_url = reverse_lazy('personnel')


class FilesListView(ListView):

    model = Files
    def get_queryset(self):
        return Files.objects.all()

class FilesDetailView(DetailView):
    model = Files
    template_name = 'app/files_detail.html'  # ✅ Matches your file path
    context_object_name = 'files'

class FilesCreateView(CreateView):
    model = Files
    fields = ['name', 'subject', 'file', 'file_type'
              ]
    template_name = 'app/files_create.html'

    def get_success_url(self):
        return reverse_lazy('files')

class FilesUpdateView(UpdateView):
    model = Files
    fields = ['name', 'subject', 'file', 'file_type']
    template_name = 'app/files_update.html'

    def get_success_url(self):
        return reverse_lazy('files')

class FilesDeleteView(DeleteView):
    model = Files
    template_name = 'app/files_delete.html'
    success_url = reverse_lazy('files')






class AdmissionListView(ListView):
    model = Admission
    template_name = 'app/admission_list.html'
    context_object_name = 'admissions'

# Create Admission
class AdmissionCreateView(CreateView):
    model = Admission
    fields = ['name', 'grade', 'student_number']
    template_name = 'app/admission_create.html'
    success_url = reverse_lazy('admission')  # Redirect to the list after saving

# Update Admission
class AdmissionUpdateView(UpdateView):
    model = Admission
    fields = ['name', 'grade', 'student_number', 'status']
    template_name = 'app/admission_update.html'
    success_url = reverse_lazy('admission')  # Redirect to the list after saving

# Delete Admission
class AdmissionDeleteView(DeleteView):
    model = Admission
    template_name = 'app/admission_delete.html'
    success_url = reverse_lazy('admission')  # Redirect to the list after deleting

class AdmissionDetailView(DetailView):
    model = Admission
    template_name = 'app/admission_detail.html'  # ✅ Matches your file path
    context_object_name = 'admissions'

class EnrollmentCreateView(CreateView):
    model = Admission
    form_class = EnrollmentForm
    template_name = 'app/enrollment_create.html'
    success_url = '/enrollment'  # Redirect to a success page or another view

    # Override form_valid to save data to Admission
    def form_valid(self, form):
        # This will save the form data to the Admission model
        form.save()
        return redirect(self.success_url)


class ListListView(ListView):
    template_name = 'app/list_list.html'
    context_object_name = 'list'

    def get_queryset(self):
        # Return an empty queryset or None since we're not using a single model.
        return []

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['personnel'] = Personnel.objects.all().order_by('last_name')[:5]  # Fetch latest 5 personnel
        context['teachers'] = Teacher.objects.all().order_by('last_name')[:5]

        return context




class TeacherListView(ListView):
    model = Teacher
    template_name = 'app/teacher_list.html'
    context_object_name = 'teachers'

class TeacherDetailView(DetailView):
    model = Teacher
    template_name = 'app/teacher_detail.html'
    context_object_name = 'teacher'

class TeacherCreateView(CreateView):
    model = Teacher
    fields = ['first_name', 'last_name', 'subject', 'email', 'gender', 'age', 'address', 'date_of_birth']
    template_name = 'app/teacher_create.html'
    success_url = reverse_lazy('teachers')

class TeacherUpdateView(UpdateView):
    model = Teacher
    fields = ['first_name', 'last_name', 'subject', 'email', 'gender', 'age', 'address', 'date_of_birth']
    template_name = 'app/teacher_update.html'
    success_url = reverse_lazy('teachers')

class TeacherDeleteView(DeleteView):
    model = Teacher
    template_name = 'app/teacher_delete.html'
    success_url = reverse_lazy('teachers')




class HomePageView(TemplateView):
    template_name = 'app/home.html'


class AboutPageView(TemplateView):
    template_name = 'app/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Fetch the latest 5 announcements
        context['announcements'] = Announcement.objects.all().order_by('-id')[:5]

        return context



class EnrollmentPageView(TemplateView):
    template_name = 'app/enrollment.html'


class CalendarListView(ListView):
    model = CalendarEvent  # Specify the model here
    template_name = 'app/calendar_list.html'
    context_object_name = 'events'

    # Override get_queryset to get the data
    def get_queryset(self):
        return CalendarEvent.objects.all().order_by('-start_date')[:5]



class AcademicEventListView(ListView):
    model = AcademicEvent
    context_object_name = 'academicevent'
    template_name = 'app/academicevent/academicevent_list.html'

class AcademicEventDetailView(DetailView):
    model = AcademicEvent
    context_object_name = 'academicevent'
    template_name = 'app/academicevent/academicevent_detail.html'

class AcademicEventCreateView(CreateView):
    model = AcademicEvent
    fields = ['title', 'content', 'body', 'created_by', 'visibility'
              ]
    template_name = 'app/academicevent/academicevent_create.html'


class AcademicEventUpdateView(UpdateView):
    model = AcademicEvent
    fields = ['title', 'content', 'body', 'created_by', 'visibility']
    template_name = 'app/academicevent/academicevent_update.html'

class AcademicEventDeleteView(DeleteView):
    model = AcademicEvent
    template_name = 'app/academicevent/academicevent_delete.html'
    success_url = reverse_lazy('academicevent')



def announcement_list(request):
    announcements = Announcement.objects.all()  # Get all announcements
    return render(request, 'app/announcement_list.html', {'announcements': announcements})

class AnnouncementListView(ListView):
    model = Announcement
    context_object_name = 'announcements'
    template_name = 'app/announcement.html'

    def get_queryset(self):
        return Announcement.objects.all()

class AnnouncementDetailView(DetailView):
    model = Announcement
    context_object_name = 'announcement'
    template_name = 'app/announcement_detail.html'

class AnnouncementCreateView(CreateView):
    model = Announcement
    fields = ['title', 'content', 'body', 'created_by', 'visibility'
              ]
    template_name = 'app/announcement_create.html'

    def get_success_url(self):
        return reverse_lazy('announcement')

class AnnouncementUpdateView(UpdateView):
    model = Announcement
    fields = ['title', 'content', 'body', 'created_by', 'visibility']
    template_name = 'app/announcement_update.html'

    def get_success_url(self):
        return reverse_lazy('announcement')

class AnnouncementDeleteView(DeleteView):
    model = Announcement
    template_name = 'app/announcement_delete.html'
    success_url = reverse_lazy('announcement')






class BookListView(ListView):
    model = Files  # The model from which you want to fetch data (Files)
    template_name = 'app/book_list.html'  # Template to render the data
    context_object_name = 'files'


    def get_queryset(self):
        query = self.request.GET.get('search', '')
        subject = self.request.GET.get('subject', '')  # Get selected subject

        files = Files.objects.all()

        # Filter by name if a search query is provided
        if query:
            files = files.filter(name__icontains=query)

        # Filter by subject if a subject is selected
        if subject:
            files = files.filter(subject=subject)

        return files

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['file_subject_choices'] = Files.SUBJECT_CHOICES  # Add subject choices to context
        return context



class CalendarEventListView(ListView):
    model = CalendarEvent
    template_name = 'app/calendar_event_list.html'
    context_object_name = 'events'
    ordering = ['event_name', 'start_date', 'end_date', 'description']

class CalendarEventDetailView(DetailView):
    model = CalendarEvent
    template_name = 'app/calendar_event_detail.html'
    context_object_name = 'event'

class CalendarEventCreateView(CreateView):
    model = CalendarEvent
    form_class = CalendarEventForm
    template_name = 'app/calendar_event_create.html'
    success_url = reverse_lazy('calendar_event')

class CalendarEventUpdateView(UpdateView):
    model = CalendarEvent
    form_class = CalendarEventForm
    template_name = 'app/calendar_event_update.html'
    success_url = reverse_lazy('calendar_event')

class CalendarEventDeleteView(DeleteView):
    model = CalendarEvent
    template_name = 'app/calendar_event_delete.html'
    success_url = reverse_lazy('calendar_event')