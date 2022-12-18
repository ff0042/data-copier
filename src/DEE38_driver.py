import pandas as pd
import os;
import sys;
from DEE38_read import get_json_reader;
from DEE38_write import load_db_table;

def process_table(BASE_DIR, conn, table_name):
    json_reader = get_json_reader(BASE_DIR, table_name) # create json reader to drive chunk by chunk reads
    for df in json_reader:
        load_db_table(df, conn, table_name, df.columns[0])

# can leverage test logic in read and write modules.
def main():
    BASE_DIR = os.environ.get('BASE_DIR')
    configs = dict(os.environ.items()) # pull in env variables.
    conn = f'postgresql://{configs["DB_USER"]}:{configs["DB_PASS"]}@{configs["DB_HOST"]}:{configs["DB_PORT"]}/{configs["DB_NAME"]}'
    table_names = sys.argv[1].split(',') # assume csv string passed in
    for table_name in table_names:
        process_table(BASE_DIR, conn, table_name)


if __name__ == '__main__':
    main()


