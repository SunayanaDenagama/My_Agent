import os
import sys
import subprocess


def run_python_file(working_directory: str, file_path: str, args: list = None) -> str:
    try:
        abs_working_dir = os.path.abspath(working_directory)
        abs_file_path = os.path.normpath(os.path.join(abs_working_dir, file_path))

        # 1. Security check
        if os.path.commonpath([abs_working_dir, abs_file_path]) != abs_working_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        # 2. Extension check
        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        # 3. File existence check
        if not os.path.isfile(abs_file_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        # Build execution command
        command = [sys.executable, abs_file_path]

        # Ensure args list is added cleanly
        if args:
            if isinstance(args, list):
                command.extend(args)
            elif isinstance(args, str):
                command.append(args)

        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=30,
            cwd=abs_working_dir
        )

        output = []
        if result.stdout:
            output.append(f"STDOUT:\n{result.stdout}")
        if result.stderr:
            output.append(f"STDERR:\n{result.stderr}")
        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")

        if not output:
            return "File executed successfully with no output."

        return "\n".join(output)

    except Exception as e:
        return f'Error executing Python file "{file_path}": {e}'

schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Executes a Python script file with optional command-line arguments and returns STDOUT/STDERR output",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the Python file (.py) to execute, relative to the working directory",
                },
                "args": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                    "description": "Optional list of command-line arguments to pass to the Python script",
                },
            },
            "required": ["file_path"],
        },
    },
}