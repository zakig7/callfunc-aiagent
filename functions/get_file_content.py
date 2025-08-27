import os
import config


def get_file_content(working_directory, file_path):

    target_dir = os.path.abspath(os.path.join(working_directory, file_path))
    abs_dir = os.path.abspath(working_directory)

    """
    IMPORTANT! Without this restriction, the LLM might go running amok anywhere on the machine,
    reading sensitive files or overwriting any data.
    """

    if not target_dir.startswith(abs_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target_dir):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    try:
        with open(target_dir, "r") as f:
            file_content_string = f.read(config.MAX_CHARS)
            remaining_content = f.read(1)
            if remaining_content:
                file_content_string += (f'...File "{file_path}" truncated at 10000 characters]')
        
    except Exception as e:
        return f"Error: {e}"
    
    return file_content_string