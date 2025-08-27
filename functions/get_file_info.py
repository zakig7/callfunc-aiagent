import os


def get_file_info(working_directory, directory="."):
    target_dir = os.path.abspath(os.path.join(working_directory, directory))
    abs_dir = os.path.abspath(working_directory)

    """
    IMPORTANT! Without this restriction, the LLM might go running amok anywhere on the machine,
    reading sensitive files or overwriting any data.
    """

    if not target_dir.startswith(abs_dir):
        # Using {directory} param here to preserve the user's original input
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'

    try:
        info_list = []
        for filename in os.listdir(target_dir):
            filepath = os.path.join(target_dir, filename)
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
