'''
Fahrenheit to Celsius:

Write the necessary code to read a degree in Fahrenheit from the console
then convert it to Celsius and print it to the console.

    C = (F - 32) * (5 / 9)

Output should read like - "81.32 degrees fahrenheit = 27.4 degrees celsius"


'''

F = input("please input a deg in Fahrenheit: ")
C = (int(F)-32) * (5/9)
print("temperature is ", C , " deg Celcius")
