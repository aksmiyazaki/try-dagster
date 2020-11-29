from dagster import execute_pipeline, pipeline, solid, InputDefinition, OutputDefinition, Output

@solid(
    output_defs=[
        OutputDefinition(name="name", dagster_type=str)
    ]
)
def get_name(_):
    yield Output('dagster', output_name="name")

@solid(
    output_defs=[
        OutputDefinition(name="age", dagster_type=int)
    ]
)
def get_age(_):
    yield Output(25, output_name="age")


### Input Types can be defined this way
@solid(
    input_defs=[
        InputDefinition(name="name", dagster_type=str),
        InputDefinition(name="age", dagster_type=int),
    ]
)
def hello(context, name, age):
    context.log.info('Hello, {name} {age}!'.format(name=name, age=age))



@pipeline
def hello_pipeline():
    n = get_name()
    a = get_age()
    hello(n, a)
