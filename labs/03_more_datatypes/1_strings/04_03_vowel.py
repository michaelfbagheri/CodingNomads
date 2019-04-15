'''
Write a script prints the number of times a vowel is used in a user inputted string.

'''

vowels = 'aeiouAEIOU'

input_String = input('please input your string of choice: ')

position = 0
num_vowel_used = 0

for i in input_String:
    position = position + 1
    for j in vowels:
        if j == i:
            num_vowel_used = num_vowel_used + 1

print('vowels were used ', num_vowel_used, ' times in ', input_String)







