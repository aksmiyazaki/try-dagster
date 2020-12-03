from dagster import *

@solid
def read_file(_, file_path: String) -> List[String]:
    with open(file_path, "r") as f:
        yield Output(f.readlines())

@solid(
    config_schema={"phrase_param": String}
)
def count_file_lines_and_show(context, file_lines: List[String]) -> Nothing:
    c = len(file_lines)
    context.log.info('This file has, {c} lines! and the phrase is {p}'.format(c=c, p=context.solid_config["phrase_param"]))

@pipeline
def broken_type_pipeline():
    count_file_lines_and_show(read_file())
