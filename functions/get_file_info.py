import os
from google.genai import types


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)


def get_file_info(working_directory, directory="."):

    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, directory))

    """
    IMPORTANT! Without this restriction, the LLM might go running amok anywhere on the machine,
    reading sensitive files or overwriting any data.
    """

    if not abs_file_path.startswith(abs_working_dir):
        # Using {directory} param here to preserve the user's original input
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(abs_file_path):
        return f'Error: "{directory}" is not a directory'

    try:
        info_list = []
        for filename in os.listdir(abs_file_path):
            filepath = os.path.join(abs_file_path, filename)
            is_dir = os.path.isdir(filepath)
            filesize = os.path.getsize(filepath)
            # Retrun a full formatted string for each filename
            info_list.append(
                f"- {filename}: file_size={filesize} bytes, is_dir={is_dir}"
            )
    except Exception as e:
        return f"Error: {e}"
    
    # Combine all strings in output_list into one final string       
    return "\n".join(info_list)
