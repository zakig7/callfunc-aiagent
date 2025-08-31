from google.genai import types

from functions.get_file_info import schema_get_files_info

# Bundle schemas into a Tool
available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
    ]
)