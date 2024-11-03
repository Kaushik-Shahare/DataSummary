import pandas as pd
from django.core.mail import send_mail
import os

EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_SEND_TO = os.environ.get('EMAIL_SEND_TO')

def process_file(file):
    # Read the file
    df = pd.read_excel(file) if file.name.endswith('.xlsx') else pd.read_csv(file)

    df.columns = df.columns.str.strip()  
    df.columns = df.columns.str.replace(' ', '_')  
    
    summary_df = df.groupby(['Cust_State', 'Cust_Pin']).size().reset_index(name='Count')
    
    summary = summary_df.to_dict(orient='records')

    print("Summary computed successfully")
    send_summary_email(summary)
    return summary

def send_summary_email(summary):
    subject = "Python Assignment - Kaushik Shahare"
    message = "Summary:\n" + "\n".join([f"{item['Cust_State']} {item['Cust_Pin']} - {item['Count']}" for item in summary])

    send_mail(
        subject,
        message,
        EMAIL_HOST_USER,
        [EMAIL_SEND_TO],
    )