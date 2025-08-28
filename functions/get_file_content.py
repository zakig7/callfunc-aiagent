import os
from config import MAX_CHARS


def get_file_content(working_directory, file_path):

    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    """
    IMPORTANT! Without this restriction, the LLM might go running amok anywhere on the machine,
    reading sensitive files or overwriting any data.
    """

    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    try:
        with open(abs_file_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            # More efficient stream-based for very large files. No need to read
            # the entire file's metadata just to get its size
            remaining_content = f.read(1)
            if remaining_content:
                file_content_string += (
                    f'...File "{file_path}" truncated at 10000 characters]'
                )
        
    except Exception as e:
        return f"Error: {e}"
    
    return file_content_string