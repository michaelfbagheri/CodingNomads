'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.



'''

my_string = input('please type your string: ')

my_string = my_string.split()

print(my_string)

for i in my_string:
    print(i, ' appears ', my_string.count(i), ' many times')




