from dagster import execute_pipeline, pipeline, solid

@solid
def get_name(_) -> str:
    return 'dagster'

@solid(
    config_schema={"age_param": int}
)
def get_age(_) -> int:
    return context.solid_config["age_param"]

@solid
def hello(context, name: str, age: int):
    context.log.info('Hello, {name} {age}!'.format(name=name, age=age))

@solid
def goodbye(context, name: str, age: int):
    context.log.info('GOODBYE, {name} {age}!'.format(name=name, age=age))

@pipeline
def hello_pipeline():
    n = get_name()
    a = get_age()
    hello(n, a)
