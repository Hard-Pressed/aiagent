from dotenv import load_dotenv
from google import genai
from google.genai import types
import os
import sys
from functions.get_files_info import available_functions

system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

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
    
    try:
        messages = [
            types.Content(role="user", parts=[types.Part(text=user_prompt)]),
        ]
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
            for function_call in response.function_calls:
                print(f"Calling function: {function_call.name}({function_call.args})")
        
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
