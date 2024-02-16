import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timedelta
import pandas as pd


# Function to send email
def send_email(to_email, subject, body):
    # Replace with your email configuration
    smtp_server = 'server name, e.g smtp.gmail.com'
    smtp_port = 587
    smtp_username = 'your_email'
    smtp_password = 'app password'

    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = smtp_username
    message['To'] = to_email
    message['Subject'] = subject

    # Attach the body to the email
    message.attach(MIMEText(body, 'plain'))

    # Connect to the SMTP server and send the email
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(smtp_username, to_email, message.as_string())
        print(f"Email sent successfully to {to_email}")
        return True
    except Exception as e:
        print(f"Failed to send email to {to_email}. Error: {e}")
        return False


# Read the CSV file into a DataFrame
file_path = 'emails.csv'
df = pd.read_csv(file_path)

# Flatten the DataFrame to a single list
flat_email_list = [email for sublist in df.values.tolist() for email in sublist]
# print(flat_email_list)
# Determine which elements to use today based on the current date
today = datetime.now().date()
start_index = 0
# print(start_index)
end_index = start_index + 10
# print(end_index)
# Get the first ten elements for today
new_list = flat_email_list[start_index:end_index]
# print(new_list)

# Replace placeholders with your actual email content
file_path_email_subject = 'directory path'
with open(file_path_email_subject) as subject_content:
    email_subject = subject_content.read()
file_path_email_body = 'directory path'
with open(file_path_email_body, encoding="utf-8") as body_content:
    email_body = body_content.read()

# Send emails and update new_list
for email in new_list:
    send_email(email, email_subject, email_body)

# Update flat_email_list with the next elements for tomorrow
flat_email_list = flat_email_list[end_index:]
# print(flat_email_list)

# Save the updated flat_email_list for the next day
# This is just a basic example; you may want to store it in a more persistent manner (e.g., database)
# flat_email_list can also be loaded from a saved file on subsequent runs
print("Remaining emails in flat_email_list:", flat_email_list)
# Open the emails.csv and rewrite the entire csv file with updated flat_email_list
with open('emails.csv', 'w+') as f:
    f.close()
with open('emails.csv', "w") as email_file:
    for email in flat_email_list:
        email_file.write(email + "\n")
