from django.db import models

class Instructor(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    contact_info = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField(auto_now_add=True)
    duration_weeks = models.IntegerField()
    instructor = models.ForeignKey(Instructor, on_delete=models.SET_NULL, null=True, blank=True)
    about = models.TextField(blank=True)  # Adding an "about" field
    skills = models.ManyToManyField(Skill, blank=True)  # Adding a Many-to-Many relationship for skills

    def __str__(self):
        return self.title


class Module(models.Model):
    title = models.CharField(max_length=200)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)  # No related_name here

    def __str__(self):
        return self.title






class Lesson(models.Model):
    LESSON_TYPES = (
        ('lecture', 'Lecture'),
        ('project', 'Project'),
        ('quiz', 'Quiz'),
        ('article', 'Article'),
    )

    title = models.CharField(max_length=200)
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='lessons')
    lesson_type = models.CharField(max_length=10, choices=LESSON_TYPES)
    content = models.TextField()

    def __str__(self):
        return self.title





class Enrollment(models.Model):
    name = models.CharField(max_length=100)  # Replace 'user' with 'name' for the enrolled person's name
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateTimeField(auto_now_add=True)
    completion_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Enrollment in {self.course.title} by {self.name}"
