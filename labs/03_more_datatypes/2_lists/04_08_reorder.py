'''
Read in 10 numbers from the user. Place all 10 numbers into an list in the order they were received.
Print out the second number received, followed by the 4th, then the 6th, then the 8th, then the 10th.
Then print out the 9th, 7th, 5th, 3rd, and 1st.

Example input: 1,2,3,4,5,6,7,8,9,10
Example output: 2,4,6,8,10,9,7,5,3,1

'''

our_array = []


for x in range(3):
    our_array.append(input('please enter a number: '))

odd_list = []
even_list = []

for i in range(len(our_array)):
    temp = int(our_array[i]) % 2
    if temp == 0:
        even_list.append(our_array[i])
    if temp == 1:
        odd_list.append(our_array[i])


print('the odd numbers within your list are: ', odd_list)
print('the event numbers within your list are: ', even_list)









