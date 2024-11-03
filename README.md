
# Project Documentation

## Overview

This documentation outlines the approach I took to develop the DevTest application, a Django web application that processes uploaded Excel and CSV files to summarize customer data by state and pin code and sends email reports of the summaries.

## Table of Contents

- [Project Documentation](#project-documentation)
  - [Overview](#overview)
  - [Table of Contents](#table-of-contents)
  - [Project Structure](#project-structure)
  - [Technologies Used](#technologies-used)
  - [Application Flow](#application-flow)
  - [Detailed Approach](#detailed-approach)
    - [File Upload Handling](#file-upload-handling)
    - [Data Processing](#data-processing)
    - [Email Notification](#email-notification)
    - [Error Handling](#error-handling)
  - [Conclusion](#conclusion)

## Project Structure

The project structure is organized as follows:

```
DevTest/
│
├── devTest/
│   ├── init.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
├── file_upload/
│   ├── migrations/
│   ├── templates/
│   │   └── file_upload/
│   │       └── upload.html
│   ├── init.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   └── utils.py
│
│
├── manage.py
└── requirements.txt
```

## Technologies Used

- **Django**: A high-level Python web framework that enables rapid development of secure and maintainable websites.
- **Pandas**: A powerful data manipulation library for Python, used to process Excel and CSV files.
- **Bootstrap**: A front-end framework for developing responsive and mobile-first websites.
- **Email Backend**: SMTP server for sending emails.
- **Jinja Templating**: A templating engine for rendering dynamic content in Django templates.

## Application Flow

1. **User Interface**: The user navigates to the file upload page.
2. **File Upload**: The user selects and uploads an Excel or CSV file.
3. **Data Processing**: The uploaded file is processed to summarize customer data.
4. **Email Notification**: The summary is sent via email to the specified address.
5. **Display Summary**: The summary report is displayed on the web interface.

## Detailed Approach

### File Upload Handling

- The application allows users to upload Excel and CSV files through a simple web form.
- The file upload form is created using HTML and styled with Bootstrap for a user-friendly interface.
- The Django view processes the uploaded file, verifying its format and handling exceptions gracefully.
- **NOTE:** I could have used React.js or Next.js for the front-end, but as the application is small, I opted for a simple HTML form with Jinja templating for rendering and Bootstrap for styling.

### Data Processing

- The `process_file` function in `utils.py` handles the data processing:
  - **Reading the File**: It uses `pandas` to read the uploaded file, supporting both `.xlsx` and `.csv` formats.
  - **Data Cleaning**: The function strips whitespace from column names for consistency.
  - **Grouping Data**: The application groups customer data by `Cust State` and `Cust Pin`, counting occurrences to generate a summary report.
  - **Conversion**: The summary DataFrame is converted into a dictionary format for easier rendering in the template.

### Email Notification

- The `send_summary_email` function sends an email containing the summary report:
  - It formats the summary into a readable string.
  - Uses Django's `send_mail` function to send the email, which requires proper SMTP configurations in the settings.
  - Error handling is implemented to manage failures in email delivery, with appropriate messages displayed to the user.

### Error Handling

- The application includes error handling at multiple points:
  - If no file is uploaded, an error message is displayed.
  - If an unsupported file type is uploaded, an error message is shown.
  - Any exceptions during file processing or email sending are caught and logged, providing feedback to the user without crashing the application.

## Conclusion

The DevTest application successfully meets its goal of providing a platform for processing customer data files, summarizing the information, and sending it via email. The application is designed to be scalable and maintainable, with room for future enhancements based on user feedback and technological advancements.
