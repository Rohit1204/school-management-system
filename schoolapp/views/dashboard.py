from django.shortcuts import redirect, render
def home(request):
    if request.user.is_authenticated:
        if request.user.is_principal:
            return redirect('principal:principal-home')
        elif request.user.is_student:
            return redirect('student:student-home')
        
        # else:
        #     return redirect('teachers:teacher-home')
    return render(request, 'landing.html')