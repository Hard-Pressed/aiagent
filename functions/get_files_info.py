import os
from google.genai import types


def get_files_info(working_directory, directory="."):
    try:
        # Create absolute paths
        abs_working_dir = os.path.abspath(working_directory)
        full_path = os.path.abspath(os.path.join(working_directory, directory))

        # Check if the full path is outside working directory
        if not full_path.startswith(abs_working_dir):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        # Check if path exists and is a directory
        if not os.path.exists(full_path) or not os.path.isdir(full_path):
            return f'Error: "{directory}" is not a directory'

        # Build directory listing
        result = []
        for item in sorted(os.listdir(full_path)):
            item_path = os.path.join(full_path, item)
            is_dir = os.path.isdir(item_path)
            size = 0 if is_dir else os.path.getsize(item_path)
            result.append(f"- {item}: file_size={size} bytes, is_dir={is_dir}")

        return "\n".join(result)
    
    except Exception as e:
        return f"Error: {str(e)}"

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

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
    ]
)