# Code for ETL operations on Country-GDP data

# Importing the required libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import sqlite3
from datetime import datetime

# Function definitions for ETL operations
def log_progress(message):
    timestamp_format = '%Y-%h-%d-%H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    with open(log_file, 'a') as f:
        f.write(f"{timestamp} : {message}\n")
    
def extract(url, table_attribs):
    page = requests.get(url).text
    data = BeautifulSoup(page, 'html.parser')
    df = pd.DataFrame(columns=table_attribs)
    tables = data.find_all('table')
    body = tables[0].find('tbody')
    rows = body.find_all('tr')
    for row in rows:
        col = row.find_all('td')
        if len(col)>=3:
            data_dict = {'Name':col[1].find_all('a')[1]['title'], 
            'MC_USD_Billion':float(col[2].contents[0][:-1])}
            # or
            # data_dict = {'Name':[col[1].find('a', recursive=False).contents[0]], 
            # 'MC_USD_Billion':[float(col[2].contents[0].strip())]}
            df1 = pd.DataFrame(data_dict, index=[0])
            df = pd.concat([df, df1], ignore_index=True)
    return df

def transform(df, csv_path):
    df1 = pd.read_csv(csv_path)
    dict_ = df1.set_index('Currency').to_dict()['Rate']
    df['MC_GBP_Billion'] = [np.round(x*dict_['GBP'],2) for x in df['MC_USD_Billion']]
    df['MC_EUR_Billion'] = [np.round(x*dict_['EUR'],2) for x in df['MC_USD_Billion']]
    df['MC_INR_Billion'] = [np.round(x*dict_['INR'],2) for x in df['MC_USD_Billion']]
    return df

def load_to_csv(df, output_path):
    df.to_csv(output_path)

def load_to_db(df, sql_connection, table_name):
    df.to_sql(table_name, sql_connection, if_exists='replace', index=False)

def run_query(query_statement, sql_connection):
    print(query_statement)
    output_query = pd.read_sql(query_statement, sql_connection)
    print(output_query)


# Declaration of variables
url = 'https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks'
table_attribs = ['Name', 'MC_USD_Billion']
csv_path = 'Largest_banks_data.csv'
exchange_csv_path = 'exchange_rate.csv'
db_name = 'Banks.db'
table_name = 'Largest_banks'
log_file = 'code_log.txt'

# Function calls to execute the ETL process and log progress
log_progress("Preliminaries complete. Initiating ETL process.")
df = extract(url, table_attribs)
# print(df)
log_progress("Data extraction complete. Initiating Transformation process")
transformed_df = transform(df, exchange_csv_path)
# print(transformed_df)
# print(transformed_df['MC_EUR_Billion'][4])
log_progress("Data transformation complete. Initiating Loading process")
load_to_csv(transformed_df, csv_path)
log_progress("Data saved to CSV file.")
conn = sqlite3.connect(db_name)
log_progress("SQL Connection initiated.")
load_to_db(df, conn, table_name)
log_progress("Data loaded to Database as table. Running the query.")
query_statement = "SELECT * FROM Largest_banks"
run_query(query_statement, conn)
query_statement = "SELECT AVG(MC_GBP_Billion) FROM Largest_banks"
run_query(query_statement, conn)
query_statement = "SELECT Name from Largest_banks LIMIT 5"
run_query(query_statement, conn)
log_progress("Process Complete.")
conn.close()
log_progress("Server Connection closed")
