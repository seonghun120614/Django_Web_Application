from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('survey/', include('survey.urls')),
    path('admin/', admin.site.urls)
]
