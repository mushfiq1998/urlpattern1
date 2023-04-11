from django.contrib import admin
from django.urls import path
# Import views.py file from current directory
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('learndj/', views.learn_django),
    path('learnpy/', views.learn_python),
]
