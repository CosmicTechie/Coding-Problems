''' One programming language has the following keywords that cannot be used as identifiers: '''

# break, case, continue, default, defer, else, for, func, goto, if, map, range, return, struct, type, var

'''Write a program to find if the given word is a keyword or not'''

keyword = {"break", "case", "continue", "default", "defer", "else", "for","func", "goto", "if", "map", "range", "return", "struct", "type", "var"}

input_var = input()
if input_var in keyword:
    print(input_var+ " is a keyword") #input_var is also a string, '+' is used for concat strings
else:
    print(input_var+ " is a not keyword")
