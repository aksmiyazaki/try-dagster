from dagster import execute_pipeline, pipeline, solid

@solid
def get_name(_):
    return 'dagster'

@solid
def get_age(_):
    return 25


@solid
def hello(context, name: str, age: int):
    context.log.info('Hello, {name} {age}!'.format(name=name, age=age))


@pipeline
def hello_pipeline():
    n = get_name()
    a = get_age()
    hello(n, a)
