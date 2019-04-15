'''
Write a script that takes a string of words and a letter from the user.
Find the index of first occurrence of the letter in the string. For example:

String input: hello world
Letter input: o
Result: 4

'''


input_String = input('please input your string of choice: ')
character_of_choice = input('please input your character of choice: ')



print('index of ', character_of_choice, ' is: ' , input_String.index(character_of_choice))