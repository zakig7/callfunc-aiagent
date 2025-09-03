from google.genai import types

from functions.get_files_info import schema_get_files_info, get_file_info
from functions.get_files_content import schema_get_file_content, get_file_content
from functions.write_files_content import schema_write_files, write_file
from functions.run_python import schema_run_python_file, run_python_file
from config import WORKING_DIR

# Bundle schemas into a Tool
available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_write_files,
        schema_run_python_file,
    ]
)


def call_function(function_call_part, verbose=False):

    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")

    function_map = {
    "get_file_content": get_file_content,
    "get_files_info": get_file_info,
    "write_files": write_file,
    "run_python_file": run_python_file,
    }

    function_name = function_call_part.name
    if function_name not in function_map:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )
    args = dict(function_call_part.args)
    args["working_directory"] = WORKING_DIR
    # Pass a dict into an arg using `keyword arguments`
    func_result = function_map[function_name](**args)
    # Return function call results, from_function_response requires
    # the response to be a dictionary, so we shove the string result into a "result" field.
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"result": func_result},
            )
        ],
    )
