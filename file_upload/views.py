from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .utils import process_file  # Assuming you have a function to process the file

class FileSummary(APIView):
    
    def get(self, request):
        return render(request, 'file_upload/upload.html')

    def post(self, request):
        if 'file' not in request.FILES:
            return render(request, 'file_upload/upload.html', {"error": "No file provided"})
        
        file = request.FILES['file']
        
        try:
            summary = process_file(file)
        except Exception as e:
            print(e)
            return render(request, 'file_upload/upload.html', {"error": str(e)})

        return render(request, 'file_upload/upload.html', {"success": "Summary computed successfully"})