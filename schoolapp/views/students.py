from django.contrib.auth import login
from django.shortcuts import redirect,render
from django.views.generic import CreateView,ListView

def StudentSignUpView(request):
    if request.method == 'POST':
        main_form = StudentSignUpForm(request.POST)
        secondary_form = StudentSignUpTwo(request.user,request.POST)
        if main_form.is_valid() and secondary_form.is_valid():
            user = main_form.save()
            secondary_form.save(request.user)
            return redirect('staff_view:staff-home')
    else:
        main_form = StudentSignUpForm()
        secondary_form = StudentSignUpTwo(request.user)
    return render(request, 'staff_view/create_student.html', {
        'main_form': main_form,
        'secondary_form': secondary_form
    })


def StudentHomeView(request):
    return render(request,'student/student_home.html')
  