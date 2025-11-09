from django.db import models
from django.contrib.auth.models import AbstractUser

# 1) Custom User model
class User(AbstractUser):
    ROLE_CHOICES = [
        ('MODULE_LEADER', 'Module Leader'),
        ('SUPERVISOR', 'Supervisor'),
        ('SECOND_MARKER', 'Second Marker'),
        ('ADMIN', 'Admin'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.username} ({self.role})"


# 2) Student model
class Student(models.Model):
    name = models.CharField(max_length=100)
    matric_id = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    programme = models.CharField(max_length=100)
    school = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.matric_id} - {self.name}"


# 3) Project model
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    level = models.CharField(max_length=50)
    rating = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title


# 4) Assignment model
class Assignment(models.Model):
    STATUS_CHOICES = [
        ('UNASSIGNED', 'Unassigned'),
        ('ASSIGNED', 'Assigned'),
        ('MODERATED', 'Moderated'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    supervisor = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name='supervisor_assignments'
    )
    marker = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name='marker_assignments'
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ASSIGNED')

    def __str__(self):
        return f"{self.student} -> {self.project}"


# 5) MarkingSheet model
class MarkingSheet(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    file_path = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Sheet for {self.assignment}"

