# Write a program that will tell whether the number entered by the user is odd or even.

user_input = int(input('Enter a number :  '))

if user_input % 2 == 0:
    print(f'{user_input} is Even ')
else:
    print(f'{user_input} is odd ')