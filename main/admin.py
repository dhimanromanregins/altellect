from django.contrib import admin
from .models import *
# Register your models here.
admin.site.site_header = "Altellect Admin"
admin.site.site_title = "Altellect Admin Portal"
admin.site.index_title = "Welcome to Altellect Admin Portal"
admin.site.register(Location)
admin.site.register(Department) 
admin.site.register(JobOpening)
admin.site.register(JobDetail)  
admin.site.register(ContactMessage)
admin.site.register(JobApplication)