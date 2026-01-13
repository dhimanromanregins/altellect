from django.db import models

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    

class JobOpening(models.Model):
    title = models.CharField(max_length=150)
    short_description = models.TextField()

    location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        related_name="jobs"
    )

    function = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name="jobs"
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.title} ({self.location})"
    

class JobDetail(models.Model):
    job = models.OneToOneField(
        JobOpening,
        on_delete=models.CASCADE,
        related_name="detail"
    )

    responsibilities = models.TextField()
    requirements = models.TextField()
    nice_to_have = models.TextField(blank=True)
    experience_required = models.CharField(max_length=100)

    def __str__(self):
        return f"Details for {self.job.title}"
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} - {self.subject}"
    

class JobApplication(models.Model):
    job = models.ForeignKey(
        "JobOpening",
        on_delete=models.CASCADE,
        related_name="applications"
    )

    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)

    resume = models.FileField(upload_to="resumes/")

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        unique_together = ("job", "email")  # prevent duplicate applies

    def __str__(self):
        return f"{self.full_name} - {self.job.title}"