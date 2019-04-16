'''
Take in 10 numbers from the user. Place the numbers in a list.
Find the largest number in the list.
Print the results.

CHALLENGE: Calculate the product of all of the numbers in the list.
(you will need to use "looping" - a concept common to list operations
that we haven't looked at yet. See if you can figure it out, otherwise
come back to this task after you have learned about loops)

'''
our_array = []


for x in range(3):
    our_array.append(input('please enter a number between 1-20: '))


print('largest number entered is: ' ,  max(our_array))


product = 0

for i in our_array:
    product = product + int(i)

print(product)



