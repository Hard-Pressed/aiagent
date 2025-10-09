from functions.get_file_content import get_file_content

def main():
    print("Testing get_file_content function")
    print("=" * 50)
    
    # Test 1: Read main.py
    print('\nTest 1: get_file_content("calculator", "main.py")')
    result1 = get_file_content("calculator", "main.py")
    if result1.startswith("Error:"):
        print(f"Error: {result1}")
    else:
        print(f"Success: Read {len(result1)} characters")
        print("File content:")
        print(result1)
    
    # Test 2: Read pkg/calculator.py
    print('\nTest 2: get_file_content("calculator", "pkg/calculator.py")')
    result2 = get_file_content("calculator", "pkg/calculator.py")
    if result2.startswith("Error:"):
        print(f"Error: {result2}")
    else:
        print(f"Success: Read {len(result2)} characters")
        print("File content:")
        print(result2)
    
    # Test 3: Try to read outside working directory
    print('\nTest 3: get_file_content("calculator", "/bin/cat")')
    result3 = get_file_content("calculator", "/bin/cat")
    if result3.startswith("Error:"):
        print(f"✓ Expected error: {result3}")
    else:
        print(f"✗ Unexpected success - should have been blocked")
    
    # Test 4: Try to read non-existent file
    print('\nTest 4: get_file_content("calculator", "pkg/does_not_exist.py")')
    result4 = get_file_content("calculator", "pkg/does_not_exist.py")
    if result4.startswith("Error:"):
        print(f"✓ Expected error: {result4}")
    else:
        print(f"✗ Unexpected success - file should not exist")

if __name__ == "__main__":
    main()