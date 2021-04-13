from airflow.contrib.hooks.aws_hook import AwsHook
from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class StageToRedshiftOperator(BaseOperator):
    ui_color = '#358140'
    sql_query = """
        COPY {}
        FROM '{}'
        ACCESS_KEY_ID '{}'
        SECRET_ACCESS_KEY '{}'
        JSON '{}'
    """

    @apply_defaults
    def __init__(self,
                 redshift_conn_id="",
                 aws_credentials_id="",
                 s3_bucket="",
                 s3_key="",
                 jsonpath="",
                 table_name="",
                 *args, **kwargs):

        super(StageToRedshiftOperator, self).__init__(*args, **kwargs)
        self.redshift_conn_id = redshift_conn_id
        self.aws_credentials_id = aws_credentials_id
        self.s3_bucket = s3_bucket
        self.s3_key = s3_key
        self.jsonpath = jsonpath
        self.table = table_name

    def execute(self, context):
        #Setting hooks and credentials
        aws_hook = AwsHook(self.aws_credentials_id)
        credentials = aws_hook.get_credentials()
        redshift = PostgresHook(postgres_conn_id=self.redshift_conn_id)
        
        #Deleting data that exists and extra step in Redshift cluster
        self.log.info("Precautionary clearing data from Redshift table if any exists (there shouldn't as the table should've just been dropped)")
        redshift.run("DELETE FROM {}".format(self.table))
        
        #Copying Sparkfy's data from Udacity S3's bucket to Redshift
        self.log.info("Copying Sparkify data from AWS environment, S3 >> Redshift")
        s3_path = "s3://{}/{}".format(self.s3_bucket, self.s3_key)
        #This conditional statement simply helps decide if the code should be staging the song data or the log data
        if self.jsonpath != "":
            jsonpath = "s3://{}/{}".format(self.s3_bucket, self.jsonpath)
            formatted_sql = StageToRedshiftOperator.sql_query.format(self.table, s3_path, credentials.access_key, credentials.secret_key, jsonpath)
        else:
            formatted_sql = StageToRedshiftOperator.sql_query.format(self.table, s3_path, credentials.access_key, credentials.secret_key, "auto")
 
         
        
        #Actually runs the conditional picking of the queries above
        self.log.info(f"Running SQL query : {formatted_sql}")
        redshift.run(formatted_sql )
        self.log.info(f"Table {self.table} has been staged successfully!!")
        