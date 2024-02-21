# Bengaluru Startup IT Companies Email Sender

## Overview

This project is a simple Python program designed to read email addresses from the `emails.csv` file, fetch email templates from the `kafka` folder, and send out personalized emails to Bengaluru startup IT companies. The `main.py` file is the main program that executes this functionality.

## Files and Directory Structure

- `emails.csv`: Contains a list of email addresses of Bengaluru startup IT companies.
- `main.py`: Python script for reading emails from `emails.csv` and sending out personalized emails.
- `kafka/`: Folder containing templates and formats for the email body and subject.

## Requirements

- Python 3.9 and above.
- Libraries: `pandas`, `smtplib`, `email`, `os`
- PythonAnywhere account for deploying and scheduling the application.

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-project.git
   ```

2. Navigate to the project directory:

   ```bash
   cd your-project
   ```

3. Install the required libraries:

   ```bash
   pip install -r requirements.txt
   ```

4. Place the list of email addresses in the `emails.csv` file.

5. Customize email templates in the `kafka` folder according to your needs.

6. Run the `main.py` script:

   ```bash
   python main.py
   ```

   This will read the email addresses from `emails.csv`, fetch templates from the `kafka` folder, and send out personalized emails.
   Note: I have limited 10 emails per day to avoid spamming. You can make required adjustments as per your choice.

## Notes

- Ensure that you have a working internet connection for sending emails using the specified SMTP server.
- Customize the SMTP server settings in the `main.py` file according to your email provider.

# Automating this program to run everyday on cloud (for free).

## Deployment on PythonAnywhere
### Uploading Files
- Log in to your PythonAnywhere account and open the Dashboard.
- Navigate to the "Files" tab.
- Create a new folder named kafka by clicking on the "New Directory" button.
- Inside the kafka folder, upload the project files (subject.txt, template.txt) from your email_job_automation project. You can do this by selecting the "Upload a file" button and choosing the files from your local machine.

### Scheduling the Task
- Go to the "Tasks" tab from the PythonAnywhere Dashboard.
- Schedule a new task by entering the command to run your script. 

  ```bash
   python3 main.py
   ```

- Set the time you want the task to run. PythonAnywhere uses UTC time, so adjust accordingly to your needs.

# Support and Contribution
For support, questions, or contributions to the email_job_automation project, please contact [arun.idk20@gmail.com] or submit an issue/pull request to the project's GitHub repository.

Remember, this README is a starting point. Depending on the specifics of your project, such as additional configuration steps, usage instructions, or dependencies, you may need to provide more detailed documentation.





