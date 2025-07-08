This script was made to help mass import users into MailWatch (web frontend for MailScanner).  
It will take a CSV of names and addresses as input, and output an SQL statement that can be used to bulk-create them as users (with default settings).
  
Usage:  
- Populate the CSV template with the users you'd like to import to MailWatch
- Copy the script to the same folder as the CSV, and run it.
- Copy the contents of the newly-created output file 'SQL_statement.sql', and execute it on MailWatch's backend.
