import os
from config import MAX_FILE_SIZE


def get_file_content(working_directory, file_path):
    try:
        # Create absolute paths
        abs_working_dir = os.path.abspath(working_directory)
        full_path = os.path.abspath(os.path.join(working_directory, file_path))

        # Check if the full path is outside working directory
        if not full_path.startswith(abs_working_dir):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        # Check if path exists and is a regular file
        if not os.path.exists(full_path) or not os.path.isfile(full_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        # Read and return file content
        with open(full_path, 'r', encoding='utf-8') as file:
            content = file.read()
            
        # Truncate if content exceeds limit
        if len(content) > MAX_FILE_SIZE:
            content = content[:MAX_FILE_SIZE]
            content += f'[...File "{file_path}" truncated at {MAX_FILE_SIZE} characters]'
            
        return content
    
    except Exception as e:
        return f"Error: {str(e)}"