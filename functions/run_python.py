import os, subprocess


def run_python_file(working_directory, file_path, args=None):
        
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
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        commands = ["python", abs_file_path]
        if args:
            commands.extend(args)
        run_result = subprocess.run(
            commands,
            cwd=abs_working_dir,
            timeout=30,
            capture_output=True,
            text=True
        )

        output = []
        if run_result.stdout:
            output.append(f"STDOUT:\n{run_result.stdout}")
        if run_result.stderr:
            output.append(f"STDERR:\n{run_result.stderr}")

        if run_result.returncode != 0:
            output.append(f"Process exited with code {run_result.returncode}")

        return "\n".join(output) if output else "No output produced."
    except Exception as e:
        return f"Error: executing Python file: {e}"
