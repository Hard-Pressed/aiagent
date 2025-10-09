from functions.get_file_content import get_file_content
from functions.write_file import write_file

def main():
    print("Testing file functions")
    print("=" * 50)
    
    # Test 5: Write to existing file (lorem.txt)
    print('\nTest 5: write_file("calculator", "lorem.txt", "wait, this isn\'t lorem ipsum")')
    result5 = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(f"Result: {result5}")
    
    # Test 6: Write to new file in subdirectory
    print('\nTest 6: write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")')
    result6 = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(f"Result: {result6}")
    
    # Test 7: Try to write outside working directory
    print('\nTest 7: write_file("calculator", "/tmp/temp.txt", "this should not be allowed")')
    result7 = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(f"Result: {result7}")

if __name__ == "__main__":
    main()