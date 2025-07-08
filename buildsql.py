import csv
import string
import random

# method to generate a random alphanumeric password
def password():
    s = (''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(12)))
    return(s)

# import csv
filename = open('Mailboxes.csv', 'r', encoding='utf-8-sig', newline='')
file = csv.DictReader(filename)

# sorts csv data into lists of names and emails
displayNames = []
emailAddresses = []
for col in file:
    displayNames.append(col['Display name'])
    emailAddresses.append(col['Email address'])

SQL_strings = []

# method for building each user's SQL string by calling password method and adding each line to a list
def make_SQL(name, email):
    SQL_string = '(\'' + (email) + '\',\'' + (password()) + '\',\'' + (name) + '\',\'U\',\'1\',\'0\',\'0\',\'0\')'
    SQL_strings.append(SQL_string)

# calls the above method for each user pulled into lists from csv
for i in range(len(emailAddresses)):
    make_SQL(displayNames[i], emailAddresses[i])

# creates output file for SQL statement
f = open('SQL_statement.sql', 'w')

# writes the format for the beginning of the full SQL statement
f.write('INSERT INTO users (username, password, fullname, type, quarantine_report, spamscore, highspamscore, noscan)\n')
f.write('VALUES\n')

# adds each user's SQL string from the arrays with a comma at the end of each line, except for the last which has a semicolon
for i in range(len(SQL_strings)):
    if i == len(SQL_strings) - 1:
        f.write(SQL_strings[i] + ';')
    else:
        f.write(SQL_strings[i] + ',\n')