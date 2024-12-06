from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views
from .views import profile, edit_profile
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('add_job/', views.add_job, name='add_job'),
    path('employer_dashboard/', views.employer_dashboard, name='employer_dashboard'),
    path('profile/', profile, name='profile'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('login_register/', views.login_register, name='login_register'),
    path('find_jobs/', views.find_jobs, name='find_jobs'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
