from django.urls import path
from .views import *
urlpatterns = [
    path("jobs/", JobOpeningListAPIView.as_view(), name="job-list"),
    path("jobs/<int:job_id>/", JobDetailAPIView.as_view(), name="job-detail"),
    path("contact/", ContactMessageCreateAPIView.as_view(), name="contact-create"),
    path("jobs/apply/", JobApplicationCreateAPIView.as_view(), name="job-apply"),
    path("locations/", LocationListAPIView.as_view(), name="location-list"),
    path("departments/", DepartmentListAPIView.as_view(), name="department-list"),

]
