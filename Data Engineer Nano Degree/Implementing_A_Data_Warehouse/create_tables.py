import configparser
import psycopg2
from sql_queries import create_table_queries, drop_table_queries

# Creates function for execution of dropping any data from tables if they are already crated
def drop_tables(cur, conn):
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()

# Creates function for execution of creating the datawarehouse schema, lined out in "sql_queries.py"
def create_tables(cur, conn):
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()

# Connects to the cluster and executes the two functions created above
def main():
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()