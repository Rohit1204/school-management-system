from django.urls import   include,path
from .views import dashboard,principal, students
 
urlpatterns = [
    path('',dashboard.home,name='home'),
    path('principal/', include(([
        path('principal-home',principal.PrincipalHomeView.as_view(),name='principal-home'),
    ], 'dashboard'),namespace='principal')),]