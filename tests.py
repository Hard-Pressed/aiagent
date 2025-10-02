from functions.get_files_info import get_files_info

def main():
    # Test 1: Current directory
    result1 = get_files_info("calculator", ".")
    print('get_files_info("calculator", "."):')
    print("Result for current directory:")
    if result1.startswith("Error:"):
        print(f"    {result1}")
    else:
        for line in result1.split('\n'):
            print(f" {line}")
    print()

    # Test 2: Subdirectory
    result2 = get_files_info("calculator", "pkg")
    print('get_files_info("calculator", "pkg"):')
    print("Result for 'pkg' directory:")
    if result2.startswith("Error:"):
        print(f"    {result2}")
    else:
        for line in result2.split('\n'):
            print(f" {line}")
    print()

    # Test 3: Absolute path outside working directory
    result3 = get_files_info("calculator", "/bin")
    print('get_files_info("calculator", "/bin"):')
    print("Result for '/bin' directory:")
    if result3.startswith("Error:"):
        print(f"    {result3}")
    else:
        for line in result3.split('\n'):
            print(f" {line}")
    print()

    # Test 4: Relative path outside working directory
    result4 = get_files_info("calculator", "../")
    print('get_files_info("calculator", "../"):')
    print("Result for '../' directory:")
    if result4.startswith("Error:"):
        print(f"    {result4}")
    else:
        for line in result4.split('\n'):
            print(f" {line}")

if __name__ == "__main__":
    main()