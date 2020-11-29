## Basic Concepts
- Solid
  - Functional unit of computtion, with defined inputs and outputs.
  - You can define Solid input types by:
    - Putting in the signature
    ```
    @solid
    def hello_variation(context, name: str, age: int)
    ```

    - Or by the input_defs decorator:
    ```
    @solid(
        input_defs=[
            InputDefinition(name="name", dagster_type=str),
            InputDefinition(name="age", dagster_type=int),
        ]
    )
    def hello(context, name, age):
    ```
    - You can also define Solid outputs.
    - You can stub inputs to solids that aren't satisfied by the pipeline topology as part of its flexible configuration facility.
    - This syntax is much better, but works only if you have 1 output:
    ```
    @solid
    def read_file(_, file_path: String) -> List[String]:
    ```
- Pipeline
  - DAGs of solids.
  - Only one pipeline per python file is allowed.
- Output
  - How a Solid compute function communicates the name and value of an output to Dagster



### Building a simple pipeline
![image](https://user-images.githubusercontent.com/18602477/100518134-8015ad80-316e-11eb-8243-4099d6c64dca.png)

Watch for the types of the parameters in the hello.

If you define a pipeline with specified types and they do not match, it will give an error with type mismatch.

![image](https://user-images.githubusercontent.com/18602477/100518313-88bab380-316f-11eb-9491-ab05a499c177.png)

To define environment, you define a yaml.
Inside the dagit, it even helps you by offering a good autocomplete.
