import numpy as np
import pandas as pd

def lambda_handler(event, context):
    query = event['Body']

    if not to_number:
        return "The function needs a 'To' number"
    elif not from_number:
        return "The function needs a 'From' number"
    elif not body:
        return "The function needs a 'Body' message to send."

	dataset = pd.read_csv('data.csv', header=0)
	keywords =  dataset.iloc[:, -1]

	datafields = {'Resource': 0,'Website': 1,'Email': 2, 'Phone': 3, 'Office Location': 4, 'Office Hours': 5, 'Info': 6}

	for index, row in keywords.iterrows():
	    if row[index] in query:
	       return dataset.iloc[datafields.get[row[index]], 'Info']

	return 'Insufficient Info'
