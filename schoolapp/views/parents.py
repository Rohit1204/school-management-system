from django.contrib.auth import login
from django.shortcuts import redirect,render
from django.views.generic import CreateView,ListView

def ParentSignUpView(request):
    if request.method == 'POST':
        main_form = ParentSignUpForm(request.POST)
        secondary_form = ParentSignUpTwo(request.user,request.POST)
        if main_form.is_valid() and secondary_form.is_valid():
            user = main_form.save()
            secondary_form.save(request.user)
            return redirect('staff_view:staff-home')
    else:
        main_form = ParentSignUpForm()
        secondary_form = ParentSignUpTwo(request.user)
    return render(request, 'staff_view/create_parent.html', {
        'main_form': main_form,
        'secondary_form': secondary_form
    })


class  ParentHomeView(ListView):
    template_name = 'parent/parent_home.html'  