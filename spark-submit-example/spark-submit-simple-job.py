from dagster import *
from dagster import ModeDefinition, execute_pipeline, pipeline
from dagster_spark import create_spark_solid, spark_resource
import datetime

@solid
def start(context) -> String:
    context.log.info("Starting flow, getting yesterday date.")
    today = datetime.date.today()
    formatted_yesterday = (today - datetime.timedelta(days=1)).strftime("%Y%m%d")
    context.log.info(f"Got yesterday date as {formatted_yesterday}")
    return formatted_yesterday


@pipeline(
    mode_defs=[ModeDefinition(resource_defs={"spark": spark_resource})]
)
def pipeline():
    yd = start()
    spark_solid = create_spark_solid("spark_process_simple_csv", "GroupedCount")
    jar_path = "/Users/alexandre.miyazaki/Documents/git-personal/try-dagster/grouped-csv-count/target/scala-2.11/grouped-csv-count.jar"
    spark_solid()
