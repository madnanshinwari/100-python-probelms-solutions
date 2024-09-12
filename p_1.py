#  Problem : User will input (3ages).Find the oldest one

Ist_age = int(input('Enter your Ist Age : '))
Second_age = int(input('Enter your Second Age : '))
Third_age = int(input('Enter your Third Age : '))

if Ist_age > Second_age:
    print(f'{Ist_age} Age is oldest one .')
elif Second_age > Third_age:
    print(f'{Second_age} Age is oldest one . ')
else:
    print(f'{Third_age} Age is oldest one .')