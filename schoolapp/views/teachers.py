from django.contrib.auth import login
from django.shortcuts import redirect,render
from django.views.generic import CreateView,ListView

def TeacherSignUpView(request):
    if request.method == 'POST':
        main_form = TeacherSignUpForm(request.POST)
        secondary_form = TeacherSignUpTwo(request.user,request.POST)
        if main_form.is_valid() and secondary_form.is_valid():
            user = main_form.save()
            secondary_form.save(request.user)
            return redirect('staff_view:staff-home')
    else:
        main_form = TeacherSignUpForm()
        secondary_form = TescherSignUpTwo(request.user)
    return render(request, 'staff_view/create_teacher.html', {
        'main_form': main_form,
        'secondary_form': secondary_form
    })


class  TeacherHomeView(ListView):
    template_name = 'teacher/teacher_home.html'  