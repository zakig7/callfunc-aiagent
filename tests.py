from functions.get_files_info import get_files_info


def test():
    result = get_files_info("calculator", ".")
    print("Result for current directory:")
    print(result)
    print("")

    result = get_files_info("calculator", "pkg")
    print("\nResult for 'pkg' directory:")
    print(result)

    result = get_files_info("calculator", "/bin") 
    print("\nResult for '/bin' directory:")
    print(result)

    result = get_files_info("calculator", "../")
    print("\nResult for '../' directory:")
    print(result)


if __name__ == "__main__":
    test()
