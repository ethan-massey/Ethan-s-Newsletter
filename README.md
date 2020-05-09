# Ethan's Newsletter
A Python application using RESTful API's, smtplib email library, and Cron job scheduling to send a weekly news/weather/quote email newsletter to a list of contacts.

# Getting Started
There are several steps you need to take to begin sending your own email newsletter:
* In email_manager.py, replace the host emails, recipient emails, and host email password. It is recommended to store these values as environment variables.
* Remember to add the needed python modules
* Edit run.sh to have the correct filepaths, and edit main.py to contain the correct path to your python interpreter

# Editing the main message
To edit the main message, simply run edit_message.py with the first argument being your new message.
* Example: ./edit_message.sh 'This is the new header message!'
* If "permission denied," run $ chmod +x edit_message.sh
* Use single quotes to surround new message parameter

# Using Cron Scheduling
It is useful to automate your emails using a cron table. Here are some commands:
* viewing your current cron table: crontab -l
* edit your cron table: crontab -e
* crontable documentation: http://man7.org/linux/man-pages/man5/crontab.5.html
