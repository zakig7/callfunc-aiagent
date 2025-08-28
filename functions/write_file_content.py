import os


def write_file(working_directory, file_path, content):

    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    """
    IMPORTANT! Without this restriction, the LLM might go running amok anywhere on the machine,
    reading sensitive files or overwriting any data.
    """

    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    try:
        if not os.path.exists(os.path.dirname(abs_file_path)):
            os.makedirs(os.path.dirname(abs_file_path), exist_ok=True)
        with open(abs_file_path, "w") as f:
            f.write(content)
            
    except Exception as e:
        return f"Error:{e}"
    # Important to return a success string so that our LLM knows
    # that the action it took actually worked. Feedback loops!
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'