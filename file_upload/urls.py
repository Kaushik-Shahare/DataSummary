from django.urls import path
from .views import *

urlpatterns = [
    path('', FileSummary.as_view(), name='file_summary'),
    
]