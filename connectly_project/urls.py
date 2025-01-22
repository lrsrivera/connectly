from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to Connectly!")

urlpatterns = [
    path('', home, name='home'),  # Root URL
    path('admin/', admin.site.urls),
    path('task_manager/', include('task_manager.urls')),  # Include the task_manager app's URLs
]
