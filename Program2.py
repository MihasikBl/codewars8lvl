def function_for_delete_string_spaces(value_string):
    string_without_spaces = ""
    for i in list(value_string):
        if i != " ":
            string_without_spaces += i
    print(string_without_spaces)

X = input("Please enter your string: ")
function_for_delete_string_spaces(X)




