'''
Write a script that takes a string of words and a symbol from the user.
Replace all occurrences of the first letter with the symbol. For example:

String input: more python programming please
Symbol input: #
Result: #ore python progra##ing please

'''

input_String = input('please input your string of choice: ')
Character_of_choice = input('please input your character of choice: ')

print(input_String[0])

input_String = input_String.replace(input_String[0],Character_of_choice)
print(input_String)
