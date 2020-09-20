from django.contrib.auth import login
from django.shortcuts import redirect,render
from django.views.generic import CreateView


def PrincipalSignUpView(request):
    if request.method == 'POST':
        main_form = PrincipalSignUpForm(request.POST)
        secondary_form = PrincipalSignUpTwo(request.user,request.POST)
        if main_form.is_valid() and secondary_form.is_valid():
            user = main_form.save()
            secondary_form.save(request.user)
            return redirect('staff_view:staff-home')
    else:
        main_form = PrincipalSignUpForm()
        secondary_form = PrincipalSignUpTwo(request.user)
    return render(request, 'staff_view/create_principal.html', {
        'main_form': main_form,
        'secondary_form': secondary_form
    })

