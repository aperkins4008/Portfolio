from datetime import datetime, timedelta
import os
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators import (StageToRedshiftOperator, LoadFactOperator, LoadDimensionOperator, DataQualityOperator)
from helpers import SqlQueries
from airflow.operators.postgres_operator import PostgresOperator



#Give AWS location variables
s3_bucket = 'udacity-dend'
song_s3 = "song_data"
log_s3 = "log_data"
log_json_file = "log_json_path.json"

#Defines the intial argugment used in the dag below
default_args = {
    'owner': 'udacity',
    'start_date': datetime(2019, 1, 12),
    'depends_on_past': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
    'catchup': False,
    'email_on_retry': False,
    'email_on_failure': False,
}

dag_name = 'udac_example_dag' 
dag = DAG('undc_dag',
          default_args=default_args, #Define Arugments
          description='Load and transform data in Redshift with Airflow',
          schedule_interval='@hourly',
          max_active_runs=1) 



start_operator = DummyOperator(task_id='Begin_execution',  dag=dag)


#Create SQL Tables (made some altering to script to drop tables if they exists)
create_tables = PostgresOperator(
    postgres_conn_id="redshift",
    task_id="create_tables",
    sql='create_tables.sql',
    dag = dag 
)


stage_events_to_redshift = StageToRedshiftOperator(
    task_id='load_stage_events',
    s3_bucket= s3_bucket,
    s3_key=log_s3,
    jsonpath=log_json_file,
    redshift_conn_id="redshift",
    aws_credentials_id="aws_credentials",
    table_name="public.staging_events",
    dag = dag,
    provide_context=True
)

stage_songs_to_redshift = StageToRedshiftOperator(
    task_id='load_stage_songs',
    s3_bucket= s3_bucket,
    s3_key=song_s3,
    redshift_conn_id="redshift",
    aws_credentials_id="aws_credentials",
    table_name="public.staging_songs",
    dag = dag,
    provide_context=True
)


load_songplays_table = LoadFactOperator(
        task_id='load_songplays_fact_table',
        redshift_conn_id="redshift",
        load_sql=SqlQueries.songplay_table_insert,
        table_name="public.songplays",
        dag=dag
)


load_user_dimension_table = LoadDimensionOperator(
        task_id='load_user_dim_table',
        redshift_conn_id="redshift",
        load_sql=SqlQueries.user_table_insert,
        table_name="public.users",
        append_only=False,
        dag=dag
)


load_song_dimension_table = LoadDimensionOperator(
    task_id='load_song_dim_table',
    redshift_conn_id="redshift",
    load_sql=SqlQueries.song_table_insert,
    table_name="public.songs",
    append_only=False,
    dag=dag
)


load_artist_dimension_table = LoadDimensionOperator(
    task_id='load_artist_dim_table',
    redshift_conn_id="redshift",
    load_sql=SqlQueries.artist_table_insert,
    table_name="public.artists",
    append_only=False,
    dag=dag
)


load_time_dimension_table = LoadDimensionOperator(
    task_id='load_time_dim_table',
    redshift_conn_id="redshift",
    load_sql=SqlQueries.time_table_insert,
    table_name="public.time",
    append_only=False,
    dag=dag
)


run_quality_checks = DataQualityOperator(
    task_id='run_data_quality_checks',
    redshift_conn_id = "redshift",
    tables = ["public.artists", "public.songplays", "public.songs", "public.time", "public.users"],
    dag=dag
    
)


    
end_operator = DummyOperator(task_id='Stop_execution',  dag=dag)


#Order of Dags
start_operator >> create_tables

create_tables >> [stage_events_to_redshift, stage_songs_to_redshift] >>load_songplays_table

load_songplays_table >> [load_user_dimension_table, load_song_dimension_table, load_artist_dimension_table, load_time_dimension_table] >> run_quality_checks

run_quality_checks >> end_operator



