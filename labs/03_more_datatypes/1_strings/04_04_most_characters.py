'''
Write a script that takes three strings from the user and prints the one with the most characters.

I'd like to know how to use an list to do this exercise
where I can push the string plus it's length into an list index and than sort that list instead of using if statements

'''

vowels = 'aeiouAEIOU'

first_string = input('please input your first string: ')
second_string = input('please input your first string: ')
third_string = input('please input your first string: ')

print(len(first_string))
print(len(second_string))
print(len(third_string))

if len(first_string) > len(second_string) and len(first_string) > len(third_string):
    print('first input : ', first_string, ' had the most characters!')

if len(second_string) > len(first_string) and len(second_string) > len(third_string):
    print('first input : ', second_string, ' had the most characters!')

if len(third_string) > len(first_string) and len(third_string) > len(second_string):
        print('first input : ', third_string, ' had the most characters!')




