'''

Using string slicing, take in the user's name and print out their name translated to pig latin.
For the purpose of this program, we will say that any word or name can be
translated to pig latin by moving the first letter to the end, followed by "ay".

For example: ryan -> yanray, caden -> adencay

'''

name = input('please enter your name: ')
first_letter = name[slice(1)]
rest_of_name = name[slice(1,len(name))]
concated_name = rest_of_name + first_letter + 'ay'
print(concated_name)
