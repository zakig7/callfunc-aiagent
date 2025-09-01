import os
from google.genai import types


def write_file(working_directory, file_path, content):

    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    """
    IMPORTANT! Without this restriction, the LLM might go running amok anywhere on the machine,
    reading sensitive files or overwriting any data.
    
    This give our LLM agent the ability to write and overwrite files.
    """

    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(abs_file_path):
        try:
            os.makedirs(os.path.dirname(abs_file_path), exist_ok=True)
        except Exception as e:
            return f"Error: creating directory: {e}"

    # Handle writes to a path that's actually a directory
    if os.path.exists(abs_file_path) and os.path.isdir(abs_file_path):
        return f'Error: "{file_path}" is a directory, not a file'
    try:
        with open(abs_file_path, "w") as f:
            f.write(content)
        # Return a success string so that our LLM knows
        # that the action it took actually worked. Feedback loops!
        return (
            f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        )
    except Exception as e:
        return f"Error: writing to file: {e}"


schema_write_files = types.FunctionDeclaration(
    name="write_files",
    description="Writes content to a file within the working directory. Creates the file if it doesn't exist.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content to write into the file.",
            ),
            "file_path": types.Schema(
                type=types.Type.STRING,
                description=" Path to the file to write, relative to the working directory."
            ),
        },
        required=["content", "file_path"]
    ),
)
