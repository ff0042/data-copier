def load_db_table(df, conn, table_name, key):
    min_key = df[key].min()
    max_key = df[key].max()
    df.to_sql(table_name, conn, if_exists='append', index=False); #append if table exists else create; do not add index. We have auto-increment/serial pk
    print(f'Loaded {table_name} for {min_key} to {max_key}')

if __name__ == '__main__':
    import pandas as pd
    import os

    users_list = [
        {'user_id':1, 'user_first_name': 'Scott', 'user_last_name': 'Tiger'},
        {'user_id':2, 'user_first_name': 'Donald', 'user_last_name': 'Duck'}
    ]

    df = pd.DataFrame(users_list) #create list of dicts
    configs = dict(os.environ.items())
    # 'postgresql://retail_user:itversity@localhost:5452/retail_db'
    conn = f'postgresql://{configs["DB_USER"]}:{configs["DB_PASS"]}@{configs["DB_HOST"]}:{configs["DB_PORT"]}/{configs["DB_NAME"]}'
    load_db_table(df, conn, 'users', 'user_id')



