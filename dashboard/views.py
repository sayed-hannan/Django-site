from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms.course_form import CourseForm
from .forms.module_form import ModuleForm
from .forms.lesson_form import LessonForm
from  courses.models import Course, Module, Instructor  # Replace with your actual model



# Create your views here.
def dashboard(request):
    return render(request, 'dashboard.html')

# def create_course(request):
#     if request.method == 'POST':
#         course_form = CourseForm(request.POST)
#         if course_form.is_valid():
#             course = course_form.save()
#             return JsonResponse({'success': True})
#         else:
#             # If the form is not valid, return validation errors in the response
#             errors = course_form.errors
#             return JsonResponse({'success': False, 'errors': errors})
#     else:
#         course_form = CourseForm()  # Create a new, empty CourseForm

#     context = {
#         'course_form': course_form,
#     }

#     return render(request, 'create_course.html', context)


from django.http import JsonResponse



from django.shortcuts import render, redirect


from .forms.course_form import CourseForm, ModuleFormSet

def create_course(request):
    course_form = CourseForm()
    module_formset = ModuleFormSet(queryset=Module.objects.none())  # An empty queryset

    if request.method == 'POST':
        course_form = CourseForm(request.POST)
        module_formset = ModuleFormSet(request.POST, queryset=Module.objects.none())

        if course_form.is_valid() and module_formset.is_valid():
            course = course_form.save()  # Save the course

            # Assign the course to each module and save them
            for form in module_formset:
                module = form.save(commit=False)
                module.course = course
                module.save()

            # Redirect or show a success message
            return redirect('success_url')

    return render(request, 'create_course.html', {
        'course_form': course_form,
        'module_formset': module_formset,
    })





def create_lesson(request):
    if request.method == 'POST':
        lesson_form = LessonForm(request.POST)
        if lesson_form.is_valid():
            lesson = lesson_form.save()
            return JsonResponse({'success': True})
        else:
            errors = lesson_form.errors
            return JsonResponse({'success': False, 'errors': errors})
    else:
        lesson_form = LessonForm()

    context = {
        'lesson_form': lesson_form,
    }

    return render(request, 'create_lesson.html', context)




def create_lesson(request):
    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to create a new Lesson
            return redirect('create_lesson')  # Redirect to the lesson list page or any other appropriate page
    else:
        form = LessonForm()  # Create a new, empty LessonForm

    return render(request, 'create_lesson.html', {'lesson_form': form})


def Instructor(request):
    if request.method == 'POST':
        course_name = request.POST['course_name']
        Course.objects.create(name=course_name)  # Replace with your actual model

    courses = Course.objects.all()  # Replace with your actual model query
    return render(request, 'instructor_profile.html', {'courses': courses})
