'''
Write a script that creates a list of all unique values in a list. For example:

list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
unique_list = [55, 'hi', 4, 13]


'''



our_list = [1, 4, 6, 55, 2, 'hi', 4, 6, 1, 55]

unique_values = list(dict.fromkeys(our_list))

print(unique_values)
