import pandas as pd;
import os;


fp = 'C:\\Users\\Lenovo\\Research\\data\\retail_db_json\\order_items\\part-r-00000-6b83977e-3f20-404b-9b5f-29376ab1419e'
## order_items_df = pd.read_json(fp, lines=True)
## 
## # Previewing data
## order_items_df.head(10)
## order_items_df.shape
## order_items_df.dtypes
## order_items_df.describe() # useful general profiling infl
## order_items_df.count()
## order_items_df.columns
## order_items_df[['order_item_id', 'order_item_order_id', 'order_item_product_id']] #projecting
## order_items_df[order_items_df['order_item_order_id'] == 2] #filtering

# dynamically reading files as dataframes
BASE_DIR = 'C:\\Users\\Lenovo\\Research\\data\\retail_db_json'
table_name = 'order_items'

# Dynamically reading files: best practice
# ----------------------------------------
# Lists all the files in the folder. 
# All our folders contain only one file.
# Hence, we can access it by reading first element in the list as below.
file_name = os.listdir(f'{BASE_DIR}/{table_name}')[0]
delim = '\\'
file_path = f'{BASE_DIR}{delim}{table_name}{delim}{file_name}'

# Read the content of the file as Pandas Dataframe.
# df = pd.read_json(file_path, lines=True)

# Reading in chunks allows use of multiple threads and avoid out of memory issues
# -------------------------------------------------------------------------------
jr = pd.read_json(file_path, lines=True, chunksize=1000) # creates JsonReader object, not a DF

# need to write a for loop around it. Use enumerate to get each df chunk and its corresponding index.
for idx, df in enumerate(jr):
   print(f'Number of records in chunk with index {idx} is {df.shape[0]}')

print ('Health check successful')