'''
Created on Jul 3, 2018

@author: Datacore
'''

import csv
 
 
def get_csv_data(csv_path):
    """
    read test data from csv and return as list
 
    @type csv_path: string
    @param csv_path: some csv path string
    @return list
    """
    rows = []
    csv_data = open(str(csv_path), "r", errors='ignore')
    content = csv.reader(csv_data)
 
    # skip header line
    next(content, None)
 
    # add rows to list
    for row in content:
        rows.append(row)
 
    return rows

