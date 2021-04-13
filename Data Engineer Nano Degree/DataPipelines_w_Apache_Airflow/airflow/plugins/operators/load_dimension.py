from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class LoadDimensionOperator(BaseOperator):

    ui_color = '#80BD9E'

    @apply_defaults
    def __init__(self,
                 redshift_conn_id="",
                 load_sql="",
                 table_name="",
                 append_only=False,
                 *args, **kwargs):

        super(LoadDimensionOperator, self).__init__(*args, **kwargs)
        self.redshift_conn_id = redshift_conn_id
        self.load_sql = load_sql
        self.table = table_name
        self.append = append_only

    def execute(self, context):
        #Create hook
        redshift = PostgresHook(postgres_conn_id=self.redshift_conn_id)
        self.log.info("Loading data into {} dimension table".format(self.table))
        self.log.info("Append mode: {}".format(self.append))
        #Determines if table has data first and if so will delete it before inserting to keep duplicates from being inserted
        if self.append:
            formatted_sql = 'INSERT INTO %s %s' % (self.table, self.load_sql)
            redshift.run(formatted_sql)
        else:
            formatted_sql = 'DELETE FROM %s' % (self.table)
            redshift.run(formatted_sql)
            formatted_sql = 'INSERT INTO %s %s' % (self.table, self.load_sql)
            redshift.run(formatted_sql)
