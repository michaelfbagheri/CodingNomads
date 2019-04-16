'''

Write a script that removes all duplicates from a list.

'''


our_array = ['a', 'a', 'b', 'b', 'c', 'd']

unique_values = []

unique_values = list(dict.fromkeys(our_array))


print(unique_values)

