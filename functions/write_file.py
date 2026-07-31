import os


def write_file(working_directory: str, file_path: str, content: str = "") -> str:
    try:
        abs_working_dir = os.path.abspath(working_directory)
        abs_file_path = os.path.normpath(os.path.join(abs_working_dir, file_path))
        if os.path.commonpath([abs_working_dir, abs_file_path]) != abs_working_dir:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if os.path.isdir(abs_file_path):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        parent_dir = os.path.dirname(abs_file_path)
        os.makedirs(parent_dir, exist_ok=True)
        with open(abs_file_path, "w", encoding="utf-8") as f:
            f.write(content)

        # Updated string format to include "characters written"
        return f'Successfully wrote {len(content)} characters written to "{file_path}"'

    except Exception as e:
        return f'Error writing to file "{file_path}": {e}'

schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Writes text content to a file relative to the working directory, creating parent directories if needed",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the file to write, relative to the working directory",
                },
                "content": {
                    "type": "string",
                    "description": "Text content to write into the file",
                },
            },
            "required": ["file_path", "content"],
        },
    },
}