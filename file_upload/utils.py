import pandas as pd
from django.core.mail import send_mail

def process_file(file):
    # Read the file
    df = pd.read_excel(file) if file.name.endswith('.xlsx') else pd.read_csv(file)
    
    df.columns = df.columns.str.strip()
    
    summary_df = df.groupby(['Cust State', 'Cust Pin']).size().reset_index(name='Count')
    
    summary = summary_df.to_dict(orient='records')
    
    print("Summary computed successfully")
    send_summary_email(summary)
    return summary

def send_summary_email(summary):
    subject = "Python Assignment - Kaushik Shahare"
    # Format the summary nicely
    message = "Summary:\n" + "\n".join([f"{item['Cust State']} {item['Cust Pin']} - {item['Count']}" for item in summary])
    
    send_mail(
        subject,
        message,
        'kaushikshahare4@gmail.com',
        ['kaushikshahare9@gmail.com'],
    )