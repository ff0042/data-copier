import pandas as pd;
import psycopg2;

# Expand columns
pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
# RESET to auto detect
pd.set_option('display.max_rows', 0)
pd.set_option('display.max_columns', 0)
pd.set_option('display.width', 0)

# validating pg setup using docker
# --------------------------------
# docker ps -a # in powershell to list all the containers. We can check status to see if Postgres container is running.

# Run the below command to start the postgres container if it is stopped
# docker start retail_pg

# Validate connectivity to the database in Postgres Server
# docker exec -it retail_pg psql -U retail_user -d retail_db -W

# Adding dependencies to requirements file. 
# psycopg2-binary==2.9.5
# SQLAlchemy==1.4.45
# pandas==1.4.4

query = 'SELECT * FROM users'
conn = 'postgresql://retail_user:itversity@localhost:5452/retail_db' # sql alchemy syntax
df = pd.read_sql(query, conn)

df

df.count()

# Writing pandas df to table
# --------------------------
# - Create list of dicts
# - Create Dataframe using list of dicts
# - Create a string type object which contains valid SQL Alchemy string to connect to Postgres Database.
# - Write the Dataframe into the table using to_sql by passing table name and connection string as arguments. 
#     * If the table is pre-created we need to use key word argument if_exists. 
#     * Also, as we would like to populate user_id using sequence, we need to disable index of Pandas Dataframe.
users_list = [
    {'user_first_name': 'Scott', 'user_last_name': 'Tiger'},
    {'user_first_name': 'Donald', 'user_last_name': 'Duck'}
]

df = pd.DataFrame(users_list) #create list of dicts

conn = 'postgresql://retail_user:itversity@localhost:5452/retail_db'
df.to_sql('users', conn, if_exists='append', index=False) # by default, this appears to autocommit.

pd.read_sql('SELECT * FROM users', conn)
