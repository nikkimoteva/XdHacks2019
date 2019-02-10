import os
import sqlite3
from PDFOCR import getInformation, getCalcium, getGlucose, getIron, getPotassium, getSodium

# TODO pandas and data_bmd
# data_bmd = pd.read_csv(data_url)

#clear bloodMD.db if it already exists
if os.path.exists('bloodMD.db'):
    os.remove('bloodMD.db')

#create a database
conn = sqlite3.connect('bloodMD.db')

#add the data to our database
data_bmd.to_sql('data_bmd', conn, dtype={
    'Title':'varchar(256)',
    'Result':'float',
    'ReferenceRange':'float',
    'Analysis':'float',
})

#row_factory: name-based access to columns returned by the query
conn.row_factory = sqlite3.Row

# Make functions to run SQL queries
def sql_query(query):
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    return rows

def sql_edit_insert(query, var):
    cur = conn.cursor()
    cur.execute(query, var)
    conn.commit()

def sql_delete(query, var):
    cur = conn.cursor()
    cur.execute(query, var)

def sql_query2(query, var):
    cur = conn.cursor()
    cur.execute(query, var)
    rows = cur.fetchall()
    return rows

getInformation()