import configparser


# CONFIG
config = configparser.ConfigParser()
config.read('dwh.cfg')

# DROP TABLES

staging_covid_case_drop = "DROP TABLE IF EXISTS staging_covidCase;"
staging_google_mobility_drop = "DROP TABLE IF EXISTS staging_googleMobility;"
demographics_drop = "DROP TABLE IF EXISTS demographics;"
covidCaseData_drop = "DROP TABLE IF EXISTS covidCaseData;"
googleMobility_drop = "DROP TABLE IF EXISTS googleMobility;"


# CREATE TABLES
# Note that the staging tables don't have contraints to ensure load

staging_covid_case_create= ("""
    CREATE TABLE IF NOT EXISTS staging_covidCase(
        Case_Type           VARCHAR(10),
        Cases               INT,
        Difference          INT,
        Date                DATE,
        Country_Region      VARCHAR(100),
        Province_State      VARCHAR(50),
        Admin2              VARCHAR(100),
        FIPS                FLOAT,
        Lat                 FLOAT,
        Long                FLOAT,
        Prep_Flow_Runtime   TIMESTAMP   
    )
""")


staging_google_mobility_create = ("""
    CREATE TABLE IF NOT EXISTS staging_googleMobility(
        country_region_code     VARCHAR(2),
        country_region          VARCHAR(100),
        sub_region_1            VARCHAR(50),
        sub_region_2            VARCHAR(100),
        date                    DATE,
        retail_and_recreation_percent_change_from_baseline    FLOAT,
        grocery_and_pharmacy_percent_change_from_baseline     FLOAT,
        parks_percent_change_from_baseline                    FLOAT,
        transit_stations_percent_change_from_baseline         FLOAT,
        workplaces_percent_change_from_baseline               FLOAT,
        residential_percent_change_from_baseline              FLOAT
    )
""")

demographics_create = ("""
    CREATE TABLE IF NOT EXISTS demographics(
        compositekey        VARCHAR         PRIMARY KEY,
        state               VARCHAR(50)     NOT NULL SORTKEY DISTKEY,
        county              VARCHAR(100)    NOT NULL,
        fips                FLOAT,
        latitude            FLOAT,
        longitude           FLOAT
    )
""")


covidCaseData_create = ("""
    CREATE TABLE IF NOT EXISTS covidCaseData(
        compositekey        VARCHAR         NOT NULL SORTKEY PRIMARY KEY,
        caseType            VARCHAR(10)     NOT NULL,
        cases               INT             NOT NULL,
        difference          INT             NOT NULL,
        date                DATE            NOT NULL
    )
""")


googleMobility_create = ("""
    CREATE TABLE IF NOT EXISTS googleMobility(
        compositekey        VARCHAR         NOT NULL SORTKEY PRIMARY KEY,
        date                DATE            NOT NULL,
        retail_and_recreation_percent_change    FLOAT       NOT NULL,
        grocery_and_pharmacy_percent_change     FLOAT       NOT NULL,
        parks_percent_change                    FLOAT       NOT NULL,
        transit_stations_percent_change         FLOAT       NOT NULL,
        workplaces_percent_change               FLOAT       NOT NULL,
        residential_percent_change              FLOAT       NOT NULL
    )
""")



# VARIABLES -- added for future ease throughout ETL process, most specificially the staging tables below
CASE1 = config.get("S3", "CASE1")
CASE2 = config.get("S3", "CASE2")
CASE3 = config.get("S3", "CASE3")
GOOGLE_DATA = config.get("S3","GMR")
IAM_ROLE = config.get("IAM_ROLE","ARN")


# LOADING OF THE TWO STAGING TABLES


staging_google_mobility_copy = ("""
    COPY staging_googleMobility (country_region_code, country_region, sub_region_1, sub_region_2, date,
    retail_and_recreation_percent_change_from_baseline, grocery_and_pharmacy_percent_change_from_baseline,
    parks_percent_change_from_baseline, transit_stations_percent_change_from_baseline, workplaces_percent_change_from_baseline,
    residential_percent_change_from_baseline
                                )
    FROM {}
    CREDENTIALS 'aws_iam_role={}'
    CSV
    IGNOREHEADER 1
    COMPUPDATE OFF region 'us-west-2'
    DATEFORMAT 'auto' 
    TRUNCATECOLUMNS
    NULL AS '0';
""").format(GOOGLE_DATA, IAM_ROLE)



staging_covid_case_copy_1 = ("""
    COPY staging_covidCase (Case_Type,Cases,Difference,Date,Country_Region,Province_State,Admin2,FIPS,Lat,Long,Prep_Flow_Runtime)
    FROM {}
    CREDENTIALS 'aws_iam_role={}'
    CSV
    IGNOREHEADER 1
    COMPUPDATE OFF region 'us-west-2'
    TIMEFORMAT as 'auto'
    DATEFORMAT 'auto' 
    TRUNCATECOLUMNS
    NULL AS '0';
""").format(CASE1, IAM_ROLE)


staging_covid_case_copy_2 = ("""
    COPY staging_covidCase (Case_Type,Cases,Difference,Date,Country_Region,Province_State,Admin2,FIPS,Lat,Long,Prep_Flow_Runtime)
    FROM {}
    CREDENTIALS 'aws_iam_role={}'
    CSV
    IGNOREHEADER 1
    COMPUPDATE OFF region 'us-west-2'
    TIMEFORMAT as 'auto'
    DATEFORMAT 'auto' 
    NULL AS '0'; 
""").format(CASE2, IAM_ROLE)


staging_covid_case_copy_3 = ("""
    COPY staging_covidCase (Case_Type,Cases,Difference,Date,Country_Region,Province_State,Admin2,FIPS,Lat,Long,Prep_Flow_Runtime)
    FROM {}
    CREDENTIALS 'aws_iam_role={}'
    CSV
    IGNOREHEADER 1
    COMPUPDATE OFF region 'us-west-2'
    TIMEFORMAT as 'auto'
    DATEFORMAT 'auto' 
    NULL AS '0';
""").format(CASE3, IAM_ROLE)


# FINAL TABLES
# Note that NVL was used to handle null values

demographics_table_insert = ("""
    INSERT INTO demographics (compositekey, state, county, fips, latitude, longitude)
    SELECT  DISTINCT
            concat(concat(NVL(Province_State,'Unassigned'),'_'),NVL(Admin2,'Unassigned'))    AS compositekey,
            NVL(Province_State,'Unassigned')             AS state,
            NVL(Admin2,'Unassigned')                     AS county,
            NVL(FIPS,0)                                  AS fips,
            NVL(Lat,0)                                   AS latitude,
            NVL(Long,0)                                  AS longitude
    FROM staging_covidCase
    WHERE Country_Region = 'US'
    ORDER BY compositekey;
""")


covidCaseData_table_insert = ("""
    INSERT INTO covidCaseData (compositekey, caseType, cases, difference, date)
    SELECT  DISTINCT
            concat(concat(NVL(Province_State,'Unassigned'),'_'),NVL(Admin2,'Unassigned'))    AS compositekey,
            NVL(Case_Type,'Unassigned')                         AS caseType,
            NVL(Cases,0)                                        AS cases,
            NVL(Difference,0)                                   AS difference,
            Date                                                AS date
    FROM staging_covidCase
    WHERE Country_Region = 'US'
    ORDER BY compositekey, date;
""")


googleMobility_table_insert = ("""
    INSERT INTO googleMobility (compositekey, date, retail_and_recreation_percent_change, grocery_and_pharmacy_percent_change,
                         parks_percent_change, transit_stations_percent_change, workplaces_percent_change, residential_percent_change)
    SELECT  DISTINCT
            concat(concat(NVL(sub_region_1,'Unassigned'),'_'),REPLACE(NVL(sub_region_2,'Unassigned'), ' County', ''))  AS compositekey,
            date                                                                       AS date,
            NVL(retail_and_recreation_percent_change_from_baseline,0)                         AS retail_and_recreation_percent_change,
            NVL(grocery_and_pharmacy_percent_change_from_baseline,0)                          AS grocery_and_pharmacy_percent_change,
            NVL(parks_percent_change_from_baseline,0)                                         AS parks_percent_change,
            NVL(transit_stations_percent_change_from_baseline,0)                              AS transit_stations_percent_change,
            NVL(workplaces_percent_change_from_baseline,0)                                    AS workplaces_percent_change,
            NVL(residential_percent_change_from_baseline,0)                                   AS residential_percent_change
    FROM staging_googleMobility
    WHERE country_region_code = 'US'
    AND sub_region_1 IS NOT NULL
    AND sub_region_2 IS NOT NULL;
""")




# Prints counts for each table (this is just generally good auditing practice)
countall_staging_covidCase = ("""
    SELECT COUNT(*) FROM staging_covidCase
""")

countall_staging_googleMobility = ("""
    SELECT COUNT(*) FROM staging_googleMobility
""")

countall_demographics = ("""
    SELECT COUNT(*) FROM demographics
""")

countall_covidCaseData = ("""
    SELECT COUNT(*) FROM covidCaseData
""")

countall_googleMobility = ("""
    SELECT COUNT(*) FROM googleMobility
""")



# QUERY LISTS
drop_table_queries = [staging_covid_case_drop, staging_google_mobility_drop, demographics_drop, covidCaseData_drop, googleMobility_drop]
create_table_queries = [staging_covid_case_create, staging_google_mobility_create, demographics_create, covidCaseData_create, googleMobility_create]

copy_table_queries = [staging_covid_case_copy_1, staging_covid_case_copy_2, staging_covid_case_copy_3, staging_google_mobility_copy]
insert_table_queries = [demographics_table_insert, covidCaseData_table_insert, googleMobility_table_insert]
counting_audit_queries = [countall_staging_covidCase, countall_staging_googleMobility, countall_demographics, countall_covidCaseData, countall_googleMobility]
