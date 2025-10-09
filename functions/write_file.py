def write_file(working_directory, file_path, content):
    import os

    try:
        # Create absolute paths
        abs_working_dir = os.path.abspath(working_directory)
        full_path = os.path.abspath(os.path.join(working_directory, file_path))

        # Check if the full path is outside working directory
        if not full_path.startswith(abs_working_dir):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        # Ensure the directory exists
        dir_name = os.path.dirname(full_path)
        os.makedirs(dir_name, exist_ok=True)

        # Write content to file
        with open(full_path, 'w', encoding='utf-8') as file:
            file.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error: {str(e)}"