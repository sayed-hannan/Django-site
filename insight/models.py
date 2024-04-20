from django.db import models

class Newsletter(models.Model):
    title = models.CharField(max_length=200)        # Add a title for your newsletter
    content = models.TextField()                     # Content of the newsletter
    publication_date = models.DateTimeField(auto_now_add=True)  # Automatically set the publication date when creating a new newsletter

    def __str__(self):
        return self.title