import csv
from typing import List

def lambda_handler(event, context):
    to_number = event['To']
    from_number = event['From']
    body = event['Body']

    if not to_number:
        return "The function needs a 'To' number"
    elif not from_number:
        return "The function needs a 'From' number"
    elif not body:
        return "The function needs a 'Body' message to send."
        
    message = body.split(' ')

    for row in getData('data.csv'):
        for word in message:
            if word in row['Keywords']:
                return rowtomessage(row)
        
    return "insufficient info"

def notblank(value: str):
    return value == ''

def rowtomessage(row: List[str]):
    #used to keep track of whether both phone num and office info are available
    firstClauseComplete = False
    message = 'The ' + row['Resource']
    if row['Phone Number'] != '':
        message = message + ' phone number is ' + row['Phone Number']
        firstClauseComplete = True
    if row['Office Hours'] != '' and row['Office Location'] != '':
        #if the phone number was already present, the office loc is the second part of the sentence.
        if firstClauseComplete:
            message = message + ' , and it '
        message = message + 'is open ' + row['Office Hours'] + ' in the ' + row['Office Location'] + '.'
    message = message + row['Pertinent Info']
    if row['Website'] != '':
        message = message + '\nWebsite: ' + row['Website']
    if row['Email'] != '':
        message = message + '\nEmail: ' + row['Email']
    return message

def getData(filename: str):
    with open(filename, newline='') as data:
        cols = ['Resource', 'Website', 'Email', 'Phone Number', 'Office Location', 'Office Hours', 'Pertinent Info']
        datareader = csv.DictReader(data, restkey='Keywords', fieldnames=cols, delimiter=',')

        for row in datareader:
            yield row

