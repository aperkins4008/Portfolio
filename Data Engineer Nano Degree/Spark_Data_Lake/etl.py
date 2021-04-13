import configparser
import time
from datetime import datetime
import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, col, hour, dayofmonth, dayofweek, weekofyear, month, year
from pyspark.sql.functions import date_format, to_timestamp, from_unixtime, weekofyear
from pyspark.sql import functions as F
from pyspark.sql.types import StructType as Struct, StructField as SFld, StringType as Str, IntegerType as Int, \
                              DoubleType as Dbl, DateType as Dat, TimestampType as Tst, FloatType as Flt, LongType as Lng

# Gets configuration file
config = configparser.ConfigParser()
config.read('dl.cfg')

# Pull the AWS Keys as appropriate 
os.environ["AWS_ACCESS_KEY_ID"]= config['AWS']['AWS_ACCESS_KEY_ID']
os.environ["AWS_SECRET_ACCESS_KEY"]= config['AWS']['AWS_SECRET_ACCESS_KEY']

#Uses the spark packages to create a spark session via Hadoop on AWS
def create_spark_session():
    spark = SparkSession \
        .builder \
        .config('spark.jars.packages', 'org.apache.hadoop:hadoop-aws:2.7.0') \
        .getOrCreate()
    return spark


# Processes Song Data
def process_song_data(spark, input_data, output_data):
    """
    This function takes the song data from Udacity's S3 input file and processes it. This is done by 
    extracting the artist and songs tables and then loading it back to the S3 bucket I've created in AWS.

    Parameters:
            spark       : Spark Session
            input_data  : The S3 bucket location of song_data, think 'input'
            output_data : The S3 bucket location of the song_data, think 'ouput'
            
    """ 
    #Using print statement to understand where in spark statement we are
    print("\n Taking in song data as variable from S3's input location....")
    # get full filepath to song data file
    #song_data = input_data + 'song_data/*/*/*/*.json'
    # utilizing smaller data set to speed up execution in WorkSpace (please use commented out song_data variable above to run full etl)
    song_data = input_data + 'song_data/A/A/B/*.json'
    
    
    #Using print statement to understand where in spark statement we are
    print("\n Defining song Schema....")
    
    songSchema = Struct([SFld("artist_id",Str()), SFld("artist_latitude", Flt()),
                        SFld("artist_location",Str()), SFld("artist_longitude",Flt()),
                        SFld("artist_name",Str()), SFld("duration",Flt()),
                        SFld("num_songs",Int()), SFld("title",Str()),
                        SFld("year",Int())])
    
    
    #Using print statement to understand where in spark statement we are
    print("\n Reading song data JSON files from S3's input location....")
    # read song data file
    df = spark.read.json(song_data, schema= songSchema, mode= 'PERMISSIVE', columnNameOfCorruptRecord= 'corruptRecord').drop_duplicates()
    

    #Using print statement to understand where in spark statement we are
    print("\n Creating select statement for song data creation....")
    # extract columns to create songs table
    songs_table = df.select('title', 'artist_id', 'year', 'duration').drop_duplicates().withColumn("song_id", F.monotonically_increasing_id())
    
    
    #Using print statement to understand where in spark statement we are
    print("\n Writing parquet file for song table and partitioned by year and artist....")    
    # write songs table to parquet files partitioned by year and artist
    songs_table.write.mode('overwrite').partitionBy('year', 'artist_id').parquet(output_data + 'songs_table/')
    
    
    #Using print statement to understand where in spark statement we are
    print("\n Reading select statement for artist data creation....") 
    # extract columns to create artists table
    artists_table = df.select('artist_id', 'artist_name', 'artist_location', 'artist_latitude', 'artist_longitude').where(df.artist_id != None).drop_duplicates()
    

    #Using print statement to understand where in spark statement we are
    print("\n Writing parquet file for artist table....")
    # write artists table to parquet files
    artists_table.write.mode('overwrite').parquet(output_data + 'artists_table/')


#Processes Log Data
def process_log_data(spark, input_data, output_data):
    
    """
    This function takes the log data from Udacity's S3 input file and processes it. This is done by 
    extracting the user, time and songplay tables and then loading it back to the S3 buckegt I've created in AWS.
   
    Parameters:
            spark       : Spark Session
            input_data  : The S3 bucket location of song_data, think 'input'
            output_data : The S3 bucket location of the song_data, think 'ouput'
    """ 
    
    #Using print statement to understand where in spark statement we are
    print("\n Taking in log data as variable from S3's input location....")
    # get full filepath to song data file
    #log_data = input_data + 'log_data/*/*/*.json'
    #utilizing exact folder set of data set to speed up execution in WorkSpace (please use commented out log_data variable above to run full etl with wildcards)
    log_data = input_data + 'log_data/2018/11/*.json'
    
    
    #Using print statement to understand where in spark statement we are
    print("\n Defining log Schema....")
    log_schema = Struct([SFld("artist", Str()), SFld("auth", Str()),
                         SFld("firstName", Str()), SFld("gender", Str()),
                         SFld("itemInSession", Lng()), SFld("lastName", Str()),
                         SFld("length", Dbl()), SFld("level", Str()),
                         SFld("location", Str()), SFld("method", Str()),
                         SFld("page", Str()), SFld("registration", Dbl()),
                         SFld("sessionId", Lng()), SFld("song", Str()),
                         SFld("status", Str()), SFld("ts", Str()),
                         SFld("userAgent", Str()), SFld("userId", Str())])
    
    
    #Using print statement to understand where in spark statement we are
    print("\n Reading log data JSON files from S3's input location....")
    # read log data file
    df = spark.read.json(log_data, schema = log_schema, mode='PERMISSIVE', columnNameOfCorruptRecord='corruptRecord').drop_duplicates()
    
    
    #Using print statement to understand where in spark statement we are
    print("\n Filtering page by NextSong....")
    # filter by actions for song plays
    df = df.filter(df.page == 'NextSong').drop_duplicates()

          
    #Using print statement to understand where in spark statement we are
    print("\n Creating select statement for users data creation....")     
    # extract columns for users table    
    users_table = df.select('userId', 'firstName', 'lastName', 'gender', 'level').where(df.userId != None).drop_duplicates()
    
          
    #Using print statement to understand where in spark statement we are
    print("\n Writing parquet file for users table....")
    # write users table to parquet files
    users_table.write.mode('overwrite').parquet(output_data + 'users_table/')
          
          
    #Using print statement to understand where in spark statement we are
    print("\n Creating timeStamp variable....")
    # create timestamp column from original timestamp column
    df = df.withColumn("timestamp", to_timestamp(from_unixtime(col("ts") / 1000)))
      
    
    #Using print statement to understand where in spark statement we are
    print("\n Creating select statement for time data creation....")      
    # extract columns to create time table
    time_table = ( df.select("timestamp").withColumn("hour", hour("timestamp")).withColumn("day", dayofmonth("timestamp")) \
                    .withColumn("week", weekofyear("timestamp")).withColumn("weekday", dayofweek("timestamp")).withColumn("weekdayName", date_format("timestamp", "E")) \
                    .withColumn("month", month("timestamp")).withColumn("year", year("timestamp")).drop_duplicates()
                 )
    
    
    #Using print statement to understand where in spark statement we are
    print("\n Writing parquet file for time table and partitioned by year and month....")        
    # write time table to parquet files partitioned by year and month
    time_table.write.mode('overwrite').partitionBy('year', 'month').parquet(output_data + 'time_table/')

          
    #Using print statement to understand where in spark statement we are
    print("\n Reading song data JSON files from S3's input location....")      
    # read in song data to use for songplays table
    song_df = spark.read.parquet(output_data + 'songs_table/')

          
    #Using print statement to understand where in spark statement we are
    print("\n Creating select statement for song play data creation....")       
    # extract columns from joined song and log datasets to create songplays table 
    songplays_table = df.withColumn('songplayId', F.monotonically_increasing_id()).join(song_df, song_df.title == df.song) \
                        .select('songplayId', col('timestamp').alias('start_time'), col('userId'),
                         'level', 'song_id', 'artist_id', col('sessionId'), 'location', col('userAgent'))
    
    
    songplays_table = songplays_table.join(time_table, songplays_table.start_time == time_table.timestamp, how="inner")\
                                     .select("songplayId", songplays_table.start_time, "userId", "level", "song_id", "artist_id", "sessionId", "location", "userAgent", "month", "year").drop_duplicates()

    
    
          
    #Using print statement to understand where in spark statement we are
    print("\n Writing parquet file for song paly table and partitioned by year and month....")       
    # write songplays table to parquet files partitioned by year and month
    songplays_table.write.mode('overwrite').partitionBy("year", "month").parquet(output_data + 'songplays_table/')


#Runs the above two functions
def main():
    spark = create_spark_session()
    #Udacity's S3 bucket
    input_data = "s3a://udacity-dend/"
    #Personal S3 Bucket
    output_data = "s3a://ap-dautm-nano-degree/"
    
    process_song_data(spark, input_data, output_data)    
    process_log_data(spark, input_data, output_data)
    print("\n ETL process completed successfully without hard errors or exceptions!")

if __name__ == "__main__":
    main()
