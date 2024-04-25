import mysql.connector
import numpy as np
conn = mysql.connector.connect(host='localhost', user='user', password='12345', database='NNCDB')
cursor = conn.cursor()
refcode = str(input("refcode:"))
query = 'SELECT ID FROM REFCODES WHERE REFCOD_CCDC = %s'
cursor.execute(query, (refcode,))
ID = cursor.fetchall()[0][0]
query = 'SELECT CIF_FILE FROM CIFS WHERE ID = %s'
cursor.execute(query, (int(ID),))
content = cursor.fetchall()[0][0]
with open(f'{refcode}.cif', 'w') as cif:
    cif.write(content)
cursor.close()
conn.close()

