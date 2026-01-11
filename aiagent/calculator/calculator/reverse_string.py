def reverse_string(s):
    return s[::-1]

if __name__ == "__main__":
    test_string = "Hello, World!"
    reversed_string = reverse_string(test_string)
    print(f"Original string: {test_string}")
    print(f"Reversed string: {reversed_string}")
