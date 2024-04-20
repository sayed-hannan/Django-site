from django.db import models

class Instructor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Course(models.Model):
    DIFFICULTY_CHOICES = (
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
    )

    TITLE_MAX_LENGTH = 255

    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    description = models.TextField()
    difficulty_level = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES)
    certificate_of_completion = models.BooleanField(default=False)
    time_to_complete_hours = models.DecimalField(max_digits=5, decimal_places=2)
    prerequisite = models.TextField(blank=True, null=True)
    about_course = models.TextField()
    skills_included = models.TextField()
    fee_type = models.CharField(max_length=10, choices=[('free', 'Free'), ('paid', 'Paid')])
    num_lessons = models.PositiveIntegerField(default=0)
    num_projects = models.PositiveIntegerField(default=0)
    num_quizzes = models.PositiveIntegerField(default=0)

    # Relationships
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, through='Enrollment')

    def __str__(self):
        return self.title

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateField()

    def __str__(self):
        return f"{self.student} enrolled in {self.course} on {self.enrollment_date}"
