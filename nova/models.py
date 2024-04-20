from django.db import models

class Subscription(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subscribe_news = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"{self.name} - {self.email} (Subscribed: {self.subscribe_news})" # Display email in admin panel or elsewhere



# Contact form
class ContactFormSubmission(models.Model):
    # CATEGORY_CHOICES = [
    #     ('feedback', 'Feedback / Questions about our online courses'),
    #     ('speaking', 'Speaking engagement for Andrew Ng'),
    #     ('press', 'Press or interview request'),
    #     ('advice', 'Entrepreneurship or career advice'),
    #     ('other', 'Other'),
    # ]




    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    # category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"