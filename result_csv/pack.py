import pandas as pd
import numpy as np
import mysql.connector
import re

data = pd.read_csv('cubic_groups.csv')


conn = mysql.connector.connect(host='localhost', user='user', password='12345', database='NNCDB')
cursor = conn.cursor()
IDs = []
i = 1
for code in data['REFCODE']:
    query = 'SELECT ID FROM REFCODES WHERE REFCOD_CCDC = %s'
    cursor.execute(query, (code,))
    resp_res = cursor.fetchall()
    IDs.append(resp_res[0][0])
    print(f"{i}) {resp_res[0][0]}")
print(IDs)
cursor.close()
conn.close()