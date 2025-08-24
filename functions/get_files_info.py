import os

def get_files_info(working_directory, directory="."):
    directory = os.path.join(working_directory, directory)

    """
    IMPORTANT! Without this restriction, the LLM might go running amok anywhere on the machine,
    reading sensitive files or overwriting any data.
    """

    if not os.path.abspath(directory).startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    elif os.path.isdir(directory) is False:
        return f'Error: "{directory}" is not a directory'
    else:
        is_dir = True
        output_list = []
        try:
            for i in os.listdir(directory):
                filepath = os.path.join(directory, i)
                # Assess for every "i" wether file or directory
                is_dir = os.path.isdir(filepath)

                # Detrmine file size and handle exception
                filesize = 0
                if not is_dir:
                    try:
                        filesize = os.path.getsize(filepath)
                    except Exception as e:
                        return f"Error: Could not get size of {i}: {e}"
                # Retrun a full formatted string for each i
                item_string = f"- {i}: file_size={filesize} bytes, is_dir={is_dir}"
                output_list.append(item_string)
        except Exception as e:
            return f"Error:{e}"
        
        # Combine all strings in output_list into one final string       
        return "\n".join(output_list)
