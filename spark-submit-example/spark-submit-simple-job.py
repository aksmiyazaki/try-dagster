from dagster import *
from dagster import ModeDefinition, execute_pipeline, pipeline, execute_solid
from dagster_spark import create_spark_solid, spark_resource
import datetime
import os

@pipeline(
    mode_defs=[ModeDefinition(resource_defs={"spark": spark_resource})]
)
def pipeline():
    today = datetime.date.today()
    formatted_yesterday = (today - datetime.timedelta(days=1)).strftime("%Y%m%d")
    os.environ["APPLICATION_PARAMS"] = f"--app-name CountCSV --input-csv-path /tmp/aksmiyazaki/dummy.csv --group-column name --output-data-path /tmp/aksmiyazaki/{formatted_yesterday}"

    spark_solid = create_spark_solid("spark_process_simple_csv", "GroupedCount")
    spark_solid()
