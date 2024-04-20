from django.shortcuts import render
# from formtools.wizard.views import SessionWizardView
from .forms.course_form import TitleDescriptionForm, DateDurationAboutForm, SkillsForm, InstructorForm
from courses.models import Course  # Import your Course model

FORMS = [
    ("step1", TitleDescriptionForm),
    ("step2", DateDurationAboutForm),
    ("step3", SkillsForm),
    ("step4", InstructorForm),
]

class CourseWizardView(SessionWizardView):
    template_name = "course_wizard.html"
    form_list = FORMS

    def done(self, form_list, **kwargs):
        # Process the submitted data from all forms
        # You can access the form data from form_list and perform actions as needed
        # For example, you can save the data to the database here

        # Assuming you have a Course model, you can create and save an instance like this:
        course = Course(
            title=form_list[0].cleaned_data['title'],
            description=form_list[0].cleaned_data['description'],
            start_date=form_list[1].cleaned_data['start_date'],
            duration_weeks=form_list[1].cleaned_data['duration_weeks'],
            about=form_list[1].cleaned_data['about'],
            # Add other fields as needed
        )
        course.save()

        # Render the 'wizard_done.html' template with a context if needed
        return render(self.request, "wizard_done.html")
