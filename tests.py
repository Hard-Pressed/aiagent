from functions.run_python_file import run_python_file

def main():
    print("Testing run_python_file function")
    print("=" * 50)
    
    # Test 1: Run main.py without arguments (should show usage)
    print('\nTest 1: run_python_file("calculator", "main.py")')
    result1 = run_python_file("calculator", "main.py")
    print(f"Result:\n{result1}")
    
    # Test 2: Run main.py with arguments (should calculate 3 + 5)
    print('\nTest 2: run_python_file("calculator", "main.py", ["3 + 5"])')
    result2 = run_python_file("calculator", "main.py", ["3 + 5"])
    print(f"Result:\n{result2}")
    
    # Test 3: Try to run tests.py (should work if it's a valid Python file)
    print('\nTest 3: run_python_file("calculator", "tests.py")')
    result3 = run_python_file("calculator", "tests.py")
    print(f"Result:\n{result3}")
    
    # Test 4: Try to run outside working directory
    print('\nTest 4: run_python_file("calculator", "../main.py")')
    result4 = run_python_file("calculator", "../main.py")
    print(f"Result:\n{result4}")
    
    # Test 5: Try to run non-existent file
    print('\nTest 5: run_python_file("calculator", "nonexistent.py")')
    result5 = run_python_file("calculator", "nonexistent.py")
    print(f"Result:\n{result5}")

if __name__ == "__main__":
    main()