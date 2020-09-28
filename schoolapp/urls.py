from django.urls import   include,path
from .views import dashboard,principal, students,teachers ,parents
urlpatterns = [
    path('',dashboard.home,name='home'),
    path('principal/', include(([
        path('principal-home',principal.PrincipalHomeView.as_view(),name='principal-home'),
    ], 'dashboard'),namespace='principal')),

    path('student/', include(([
        path('student-home',students.StudentHomeView,name='student-home'),
    ], 'dashboard'),namespace='student')),

    path('teacher/', include(([
        path('teacher-home',teachers.TeacherHomeView.as_view(),name='teacher-home'),
    ], 'dashboard'),namespace='teacher')),
    
   path('parent/', include(([
        path('parent-home',parents.ParentHomeView.as_view(),name='parent-home'),
    ], 'dashboard'),namespace='parent')),    
    
    ]