from dagster import execute_pipeline, pipeline, solid, InputDefinition

@solid
def get_name(_):
    return 'dagster'

@solid
def broken_get_name(_):
    return 123

@solid
def get_age(_):
    return 25


### Input Types can be defined this way
@solid(
    input_defs=[
        InputDefinition(name="name", dagster_type=str),
        InputDefinition(name="age", dagster_type=int),
    ]
)
def hello(context, name, age):
    context.log.info('Hello, {name} {age}!'.format(name=name, age=age))


### This way also works as expected
@solid
def hello_variation(context, name: str, age: int):
    context.log.info('Hello, {name} {age}!'.format(name=name, age=age))

# @pipeline
# def hello_pipeline():
#     n = get_name()
#     a = get_age()
#     hello(n, a)

# @pipeline
# def hello_pipeline():
#     n = get_name()
#     a = get_age()
#     hello_variation(n, a)
#
#
@pipeline
def broken_type_pipeline():
    n = broken_get_name()
    a = get_age()
    hello(n, a)
