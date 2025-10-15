from dotenv import load_dotenv
from google import genai
from google.genai import types
import os
import sys
from functions.get_files_info import available_functions, get_files_info
from functions.get_file_content import get_file_content
from functions.run_python_file import run_python_file
from functions.write_file import write_file

system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

def call_function(function_call_part, verbose=False):
    functions = {
        "get_files_info": get_files_info,
        "get_file_content": get_file_content,
        "run_python_file": run_python_file,
        "write_file": write_file,
    }
    
    function_name = function_call_part.name
    
    if verbose:
        print(f"Calling function: {function_name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_name}")
    
    if function_name in functions:
        # Copy args and add working_directory
        args = function_call_part.args.copy()
        args["working_directory"] = "./calculator"
        
        # Call the function with keyword arguments
        result = functions[function_name](**args)
        
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"result": result},
                )
            ],
        )
    else:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )

def main():
    # Check if prompt was provided
    if len(sys.argv) < 2:
        print("Error: Please provide a prompt")
        print("Usage: uv run main.py \"Your prompt here\"")
        sys.exit(1)
    # Get prompt from command line argument
    user_prompt = sys.argv[1]
    verbose = "--verbose" in sys.argv
    # Load environment variables
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    
    if not api_key:
        print("Error: GEMINI_API_KEY not found in environment variables")
        sys.exit(1)
    # Initialize the Gemini client
    client = genai.Client(api_key=api_key)
    
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    
    try:
        while True:
            if verbose:
                print("User prompt:")
                print(user_prompt)
                print("\nSending request to Gemini API...")
            
            # Generate content using the specified model
            response = client.models.generate_content(
                model="gemini-2.0-flash-001",
                contents=messages,
                config=types.GenerateContentConfig(
                    system_instruction=system_prompt,
                    tools=[available_functions]
                ),
            )
            
            # Print the response
            print("\nGemini's response:")
            if response.text:
                print(response.text)
            
            # Check for function calls
            if response.function_calls:
                tool_messages = []
                for function_call in response.function_calls:
                    tool_content = call_function(function_call, verbose)
                    
                    # Validate the structure and print result if verbose
                    if verbose:
                        if (hasattr(tool_content, 'parts') and 
                            len(tool_content.parts) > 0 and 
                            hasattr(tool_content.parts[0], 'function_response') and 
                            tool_content.parts[0].function_response.response is not None):
                            print(f"-> {tool_content.parts[0].function_response.response}")
                        else:
                            raise Exception("Function call result does not have expected structure")
                    
                    tool_messages.append(tool_content)
                
                # Add tool responses to conversation
                messages.extend(tool_messages)
                # Continue the loop to get the final response
            else:
                # No more function calls, exit the loop
                break
        
        # Print token usage if verbose is used
        if verbose:
            print(f"\nPrompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
            print("\nRequest completed successfully")
    except Exception as e:
        print(f"Error generating content: {str(e)}")
        if verbose:
            import traceback
            print("\nFull error traceback:")
            print(traceback.format_exc())
if __name__ == "__main__":
    main()
