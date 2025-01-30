from importlib.metadata import files
from urllib import request

from django.contrib import admin
from .models import Announcement, Book, AcademicEvent, Calendar, Files, Admission, Teacher, Personnel, CalendarEvent

admin.site.register(AcademicEvent)
admin.site.register(Announcement)
admin.site.register(Book)
admin.site.register(Calendar)
admin.site.register(Files)
admin.site.register(Admission)

admin.site.register(Teacher)
admin.site.register(CalendarEvent)
admin.site.register(Personnel)



