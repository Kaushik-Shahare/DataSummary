from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .utils import *
from django.core.mail import send_mail  # Import send_mail for sending emails

class FileSummary(APIView):
    
    def get(self, request):
        return render(request, 'file_upload/upload.html')

    def post(self, request):
        if 'file' not in request.FILES:
            return render(request, 'file_upload/upload.html', {"error": "No file provided"})
        
        file = request.FILES['file']
        email = request.POST.get('email')
        send_report = request.POST.get('send_report') == 'on'  # Checkbox will return 'on' if checked

        try:
            summary = process_file(file)
        except Exception as e:
            print(e)
            return render(request, 'file_upload/upload.html', {"error": str(e)})

        if send_report:
            subject = "Python Assignment - Kaushik Shahare"
            message = "Summary:\n" + "\n".join([f"{item['Cust_State']} {item['Cust_Pin']} - {item['Count']}" for item in summary])

            send_mail(
                subject,
                message,
                EMAIL_HOST_USER,
                [EMAIL_SEND_TO, email],
            )

        return render(request, 'file_upload/upload.html', {
            "success": "Summary computed successfully and email sent." if send_report else "Summary computed successfully.",
            "summary": summary
        })

    def generate_report_message(self, summary):
        """Helper function to generate a report message from the summary."""
        message = "Here is your summary report:\n\n"
        for item in summary:
            message += f"State: {item['Cust_State']}, Pin: {item['Cust_Pin']}, Count: {item['Count']}\n"
        return message