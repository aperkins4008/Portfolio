import configparser
import psycopg2
from sql_queries import counting_audit_queries


def selects(cur, conn):
    """
    Get the count of all rows for the tables
    """
    for counting_query in counting_audit_queries:
        print('Executing ' + counting_query)
        cur.execute(counting_query)
        analysis = cur.fetchone()

        for row in analysis:
            print("   ", row)



if __name__ == "__main__":
    main()
    
    