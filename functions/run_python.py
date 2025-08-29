import os, subprocess


def run_python_file(working_directory, file_path, args=[]):
        
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    """
    IMPORTANT! Without this restriction, the LLM might go running amok anywhere on the machine,
    reading sensitive files or overwriting any data.
    """

    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    if not abs_file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        completed_process = subprocess.run(
            [
                "python", file_path, *args 
            ],
            cwd=abs_working_dir, timeout=30, capture_output=True, text=True
        )
    except Exception as e:
        return f"Error: executing Python file: {e}"

    if completed_process.stdout == "" and completed_process.stderr == "":
        return "No output produced"
    elif completed_process.returncode == 0:
        return f'STDOUT:\n{completed_process.stdout}\nSTDERR:\n{completed_process.stderr}'
    elif completed_process.returncode != 0:
        return f'STDOUT:\n{completed_process.stdout}\nSTDERR:\n{completed_process.stderr}\nProcess exited with code {completed_process.returncode}'