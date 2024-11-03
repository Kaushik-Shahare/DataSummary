from django.urls import path
from .views import *

urlpatterns = [
    path('summary/', FileSummary.as_view(), name='file_summary'),
    
]