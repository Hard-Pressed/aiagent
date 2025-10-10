import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    try:
        # Check if file has .py extension
        if not file_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file.'

        # Create absolute paths
        abs_working_dir = os.path.abspath(working_directory)
        full_path = os.path.abspath(os.path.join(working_directory, file_path))

        # Check if the full path is outside working directory
        if not full_path.startswith(abs_working_dir):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        # Check if the file exists
        if not os.path.isfile(full_path):
            return f'Error: File "{file_path}" not found'

        # Run the Python file with timeout
        result = subprocess.run(
            ["python", full_path] + args,
            capture_output=True,
            text=True,
            cwd=working_directory,
            timeout=30
        )

        # Format output
        output_parts = []
        if result.stdout.strip():
            output_parts.append(f"STDOUT: {result.stdout.strip()}")
        if result.stderr.strip():
            output_parts.append(f"STDERR: {result.stderr.strip()}")
        if result.returncode != 0:
            output_parts.append(f"Process exited with code {result.returncode}")
        
        if not output_parts:
            return "No output produced."
        
        return "\n".join(output_parts)

    except subprocess.TimeoutExpired:
        return "Error: Process timed out after 30 seconds"
    except Exception as e:
        return f"Error: executing Python file: {e}"