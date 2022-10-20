def reverse_string_decorator(function):
    def inner_wrap():
        func = function()
        str1, str2, str3 = func

        reverse_str1 = ''
        reverse_str2 = ''
        reverse_str3 = ''

        for letter in str1:
            reverse_str1 = letter + reverse_str1
        for letter in str2:
            reverse_str2 = letter + reverse_str2
        for letter in str3:
            reverse_str3 = letter + reverse_str3
        print("Output:",reverse_str1, reverse_str2, reverse_str3)
    return inner_wrap


def string_inputs():
    str1 = input("Enter string 1:")
    str2 = input("Enter string 2:")
    str3 = input("Enter string 3:")
    return (str1, str2, str3)

decorate = reverse_string_decorator(string_inputs)
decorate()
        