import pandas as pd;
import psycopg2;
import os

# pandas DB operations are usually a 3-step process:
# 1. Import pandas
# 2. Prapare variables
# 3. Pass to pandas db operation

conn = 'postgresql://retail_user:itversity@localhost:5452/retail_db'
pd.read_sql('SELECT * FROM departments', conn)

# dynamically reading files as dataframes
# ---------------------------------------
BASE_DIR = 'C:\\Users\\Lenovo\\Research\\data\\retail_db_json'
table_name = 'departments'

file_name = os.listdir(f'{BASE_DIR}/{table_name}')[0]
fp = f'{BASE_DIR}\\{table_name}\\{file_name}'

df = pd.read_json(fp, lines=True)

conn = 'postgresql://retail_user:itversity@localhost:5452/retail_db'
df.to_sql(table_name, conn, if_exists='append', index=False)

# validate data in table with pandas
# ---------------------------------------
query = 'SELECT * FROM departments'
conn = 'postgresql://retail_user:itversity@localhost:5452/retail_db'
df = pd.read_sql(
    query,
    conn
)

df

df.count()

pd.read_sql(
	'SELECT count(*) FROM departments', # simple sql count. Returns dataframe - note the index...
	conn
)

# Populate orders table in chunks
# ------------------------------
#   - Read data from files using read_json with chunksize set to 1000. It will create an object of type JSON Reader.
#   - Create connection string using SQL Alchemy Syntax.
#   - Iterate through JSON Reader object. In each iteration we will get a Dataframe of specified chunksize.
#   - Load Dataframe related to each chunk into the target table.
BASE_DIR = 'C:\\Users\\Lenovo\\Research\\data\\retail_db_json'
table_name = 'orders'
file_name = os.listdir(f'{BASE_DIR}/{table_name}')[0]
delim = '\\'
file_path = f'{BASE_DIR}{delim}{table_name}{delim}{file_name}'

jr = pd.read_json(file_path, lines=True, chunksize=1000) # creates JsonReader object, not a DF

# need to write a for loop around it. Use enumerate to get each df chunk and its corresponding index.
conn = 'postgresql://retail_user:itversity@localhost:5452/retail_db'
for idx, df in enumerate(jr):
   print(f'Number of records in chunk with index {idx} is {df.shape[0]}')
   df.to_sql(table_name, conn, if_exists='append', index=False)

# validate
pd.read_sql(
	'SELECT count(*) FROM orders', # simple sql count. Returns dataframe - note the index...
	conn
)

test_df = pd.read_sql(
	'SELECT * FROM orders limit 100', # simple sql count. Returns dataframe - note the index...
	conn
)

test_df

df.count()

print ('Health check successful')