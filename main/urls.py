from django.urls import path
from .views import JobOpeningListAPIView, JobDetailAPIView,ContactMessageCreateAPIView

urlpatterns = [
    path("jobs/", JobOpeningListAPIView.as_view(), name="job-list"),
    path("jobs/<int:job_id>/", JobDetailAPIView.as_view(), name="job-detail"),
    path("contact/", ContactMessageCreateAPIView.as_view(), name="contact-create"),
]
