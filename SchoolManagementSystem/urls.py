"""SchoolManagementSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include,path
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib.auth import urls
from django.contrib import admin
from django.contrib.auth import views as auth_views
from schoolapp.views import dashboard,teachers,principal,students,parents

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('schoolapp.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/student/', students.StudentSignUpView, name='student_signup'),
    path('accounts/signup/teacher/', teachers.TeacherSignUpView, name='teacher_signup'),
    path('accounts/signup/Parent/', parents.ParentSignUpView, name='parent_signup'),
    path('accounts/signup/Principal/', principal.PrincipalSignUpView, name='principal_signup') 
]

