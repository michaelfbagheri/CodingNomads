'''

Write the necessary code to display "Hello World!" 5 times.


'''


for i in ["hello", "mike"]:
    print("Hello World! ", i)

for i in range(5):
    print("Hello World! ", i )





a = [f"{i+1}:hello world" for i in range(5)]
print(a)


a = [str(i) + ": hello world"  for i in range(5)]
print(a[4])



