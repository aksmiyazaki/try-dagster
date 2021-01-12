from dagster import *
from dagster import ModeDefinition, execute_pipeline, pipeline, execute_solid
from dagster_spark import create_spark_solid, spark_resource
import datetime
import os


@solid
def get_yesterday(context) -> str:
    today = datetime.date.today()
    formatted_yesterday = (today - datetime.timedelta(days=1)).strftime("%Y%m%d")


@solid(
    name="spark-csv-read",
    config_schema=define_spark_config(),

    output_defs=[OutputDefinition(Nothing)],
    tags={"kind": "spark", "main_class": main_class},
    required_resource_keys=required_resource_keys,
)
def spark_solid(context):  # pylint: disable=unused-argument
    context.resources.spark.run_spark_job(context.solid_config, main_class)



@pipeline(
    mode_defs=[ModeDefinition(resource_defs={"spark": spark_resource})]
)
def pipeline():
    today = datetime.date.today()
    formatted_yesterday = (today - datetime.timedelta(days=1)).strftime("%Y%m%d")
    os.environ["APPLICATION_PARAMS"] = f"--app-name CountCSV --input-csv-path /tmp/aksmiyazaki/dummy.csv --group-column name --output-data-path /tmp/aksmiyazaki/{formatted_yesterday}"

    spark_solid = create_spark_solid("spark_process_simple_csv", "GroupedCount")
    spark_solid()
