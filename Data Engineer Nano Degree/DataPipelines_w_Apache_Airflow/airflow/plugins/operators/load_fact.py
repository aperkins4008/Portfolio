from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class LoadFactOperator(BaseOperator):

    ui_color = '#F98866'

    def __init__(self,
                 redshift_conn_id="",
                 load_sql="",
                 table_name="",
                 *args, **kwargs):

        super(LoadFactOperator, self).__init__(*args, **kwargs)
        self.redshift_conn_id = redshift_conn_id
        self.load_sql = load_sql
        self.table = table_name

    def execute(self, context):
        #creating hook
        redshift = PostgresHook(postgres_conn_id=self.redshift_conn_id)
        #inserting into fact table
        self.log.info("Loading data into {} fact table".format(self.table))
        formatted_sql = 'INSERT INTO %s %s' % (self.table, self.load_sql)
        redshift.run(formatted_sql)
